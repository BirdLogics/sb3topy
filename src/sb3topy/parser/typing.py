"""
typing.py

Used to determine the type of variables and procedure arguments.

Makes a directed graph, where each node is a variable or argument.

Example Node id_tuples:
    ('var', 'sprite1', 'my variable')
    ('proc_arg', 'sprite1', 'custom block %s', 'x pos')


Valid types are:
    bool, int, float, str, any

TODO Consider "used as" type detection
Useful if a variable is only used as a number

TODO Consider using known_type rather than types_set?
"""

import logging
from typing import Any, Dict, Set

from .. import config

logger = logging.getLogger(__name__)


COLORS = {
    'var': 'orange',
    'list': 'red',
    'proc_arg': 'rebeccapurple',
    'type': 'skyblue',
    'target': 'green',
    'target_fill': 'palegreen',
    'proc_fill': 'mediumpurple'
}

try:
    from graphviz import Digraph as gvDigraph
except ImportError:
    gvDigraph = None


class Node:
    """
    Represents an item of a certain type

    Attributes:
        id_tuple: A tuple providing unique identification for the node

        known_type: The known type of this node

        types_set: The types the item has been "set" to. Does not
            include the type of parent Nodes until they are resolved.

        parent_nodes: A set of nodes which this node is dependent on.

        unresolved - A shared set which this node adds and removes
            itself from depending on the unresolved status
    """

    def __init__(self, id_tuple, unresolved):
        self.id_tuple = id_tuple

        self.unresolved = unresolved
        self.unresolved.add(self)

        self.known_type = 'any'

        self.types_set = set()
        # self.get_types = set()

        self.parent_nodes: Set[Node] = set()

    def __hash__(self):
        return hash(self.id_tuple)

    def add_type(self, set_type):
        """
        Adds a type to either the internal types_set or parent_nodes

        set_type should be either str or Node
        """
        if isinstance(set_type, Node):
            self.parent_nodes.add(set_type)
        else:
            assert isinstance(set_type, str)
            self.types_set.add(set_type)

    def resolve(self, chain, loops):
        """
        Attempts to resolve the type of this node. When called with empty
        sets, the node is guaranteed to resolve to known_type. When called
        recursivly with non-empty sets, the node may or may not resolve
        depending on if there are any loops.

        chain - A set containing all nodes which have been passed through
            during resolution. Used to detect loops.

        loops - A set used to return all nodes which have been detected as a
            loop. Always an empty set when resolve is called.

        A node cannot resolve unless it is either the only node in loops, or
        loops is empty.


        Returns a set containing all the types this node is known to
        possibly produce. If there was a loop, the loop node contains the
        rest of the types the node can produce.

        Issue, nodes are never removed from loops.
        """

        if self not in self.unresolved:
            return self.known_type

        logger.debug("Resolving node %s", self.id_tuple)

        # Add self to chain to detect loops
        chain.add(self)

        # Get a set of all types this node can be
        for parent in frozenset(self.parent_nodes):
            # Don't resolve a loop
            if parent in chain:
                loops.add(parent)

            # Resolve the parent
            else:
                if parent in loops:
                    logger.warning("Type node parent in loops but not chain")

                # Loops don't matter for each parent's branch
                branch_loops = set()

                # Resolve the parent
                parent.resolve(chain, branch_loops)
                self.types_set.update(parent.types_set)

                # Remove the parent if it has resolved
                if parent not in self.unresolved:
                    self.parent_nodes.remove(parent)
                    self.types_set.add(parent.known_type)

                # Loops in the parent do matter for this branch
                loops.update(branch_loops)

        # Cannot resolve unless either loops is
        # empty or self is the only node in loops
        if not loops or (len(loops) == 1 and self in loops):
            self.force_resolve()

        # If this is part of a smaller loop but a bigger one
        # is still unresolved, resolve the bigger one first
        elif self in loops:
            loops.remove(self)

        # Remove self from chain
        chain.remove(self)

    def force_resolve(self):
        """
        Forces the node to resolve based on its current types_set.

        Should only be called after all of the node's parents have resolved.
        """
        self.known_type = self.resolve_type(self.types_set.copy())
        self.unresolved.remove(self)

        logger.debug("Resolved %s type node '%s' as '%s'",
                      self.id_tuple[0], self.id_tuple[-1], self.known_type)

    @staticmethod
    def resolve_type(types_set):
        """
        Determines what type a node should be
        based on the different types it can be.

        Values may be removed form types_set.

        # TODO Don't modify types_set?
        """

        if 'any' in types_set:
            # The return type is any too
            if not config.DISABLE_ANY_CAST:
                return 'any'

            # Cast from any to something instead
            types_set.remove('any')

        # Replace int casting with float
        if config.DISABLE_INT_CAST:
            if 'int' in types_set:
                types_set.remove('int')
                types_set.add('float')

        # Aggressive numeric casting
        if config.AGGRESSIVE_NUM_CAST:
            if 'float' in types_set:
                return 'float'

            if 'int' in types_set:
                return 'int'

        # If a single type is in the set, return it
        if len(types_set) == 1:
            return types_set.pop()

        if 'str' in types_set:
            if config.DISABLE_STR_CAST:
                return 'any'
            return 'str'

        if 'float' in types_set:
            return 'float'

        if 'int' in types_set:
            return 'int'

        if 'bool' in types_set:
            return 'bool'

        # The types_set should be empty
        if types_set:
            logger.warning("Failed to identify type of '%s'", types_set)

        return 'any'


class DiGraph:
    """
    A directed graph used to determine types.

    Attributes:
        nodes: A dict referencing nodes by their id_tuple

        unresolved: A set containing all unresolved nodes
    """

    def __init__(self):
        self.nodes: Dict[Any, Node] = {}
        self.unresolved = set()

    def add_node(self, id_tuple):
        """Creates a node from an id tuple"""
        # Verify the node hasn't been created
        if id_tuple not in self.nodes:
            self.nodes[id_tuple] = Node(id_tuple, self.unresolved)

        else:
            logger.warning("Duplicate type node %s", id_tuple)

        return self.nodes[id_tuple]

    def get_node(self, id_tuple):
        """Gets a node from an id tuple"""
        node = self.nodes.get(id_tuple)

        if node is not None:
            return node

        logger.warning("Unknown type node %s", id_tuple)
        return self.add_node(id_tuple)

    def resolve(self):
        """Resolves all nodes"""

        if config.RENDER_GRAPH:
            render = Render(self)

        logger.debug("Resolving type graph...")

        while self.unresolved:
            logger.debug("Type digraph resolution step")
            # Get and resolve an unresolved node
            next(iter(self.unresolved)).resolve(set(), set())

        if config.RENDER_GRAPH:
            render.render()


class Render:
    """
    Handles rendering a DiGraph with graphviz

    Attributes:
        digraph: The DiGraph instance being rendered
        nodes: A dict containing Nodes and their parents
        clusters: Contains clusters of nodes.

    clusters structure:
    {
        # Stage Nodes
        None: {
            None: [loose Nodes].
            'procedure name': [arg Nodes]
        },

        # Target Nodes
        'target name': {
            None: [loose Nodes],
            'procedure name': [arg Nodes]
        }
    }
    """

    def __init__(self, digraph: DiGraph):
        logger.debug("Pre-rendering type graph.")

        self.digraph = digraph

        self.nodes = {node: frozenset(node.parent_nodes)
                      for node in digraph.nodes.values()}
        self.frozen_types = {node: frozenset(node.types_set)
                             for node in digraph.nodes.values()}

        self.unique_id = 0
        self.node_ids: Dict[Node, str] = {}

        self.clusters: Dict[str, Dict[str, list]] = {}
        self._init_clusters()

    def _init_clusters(self):
        """Adds nodes in self.nodes to the clusters dict"""
        for node in self.nodes:
            target_name = node.id_tuple[1]
            proc_name = node.id_tuple[2] if node.id_tuple[0] == 'proc_arg' else None

            if target_name == 'Stage':
                cluster = self.clusters.setdefault(None, {})

            else:
                cluster = self.clusters.setdefault(target_name, {})

            cluster = cluster.setdefault(proc_name, [])

            cluster.append(node)

    def render(self):
        """Render the digraph"""

        logger.info("Rendering type graph...")

        if gvDigraph is None:
            logger.warning(
                "Cannot render type graph; graphviz not installed.")
            return

        graph = gvDigraph(engine=config.GRAPH_ENGINE)
        # graph.attr(overlap="false")

        for name, cluster in self.clusters.items():
            if name is None:
                self.render_stage(graph, cluster)
            else:
                self.render_target(graph, name, cluster)

        self.render_edges(graph)

        # graph = graph.unflatten(stagger=3)
        graph.render(view=False, directory=config.OUTPUT_PATH,
                     filename="type_graph")

    def render_stage(self, graph: gvDigraph, cluster):
        """Adds loose stage nodes to the graph"""
        for pname, subcluster in cluster.items():
            if pname is None:
                for node in subcluster:
                    self.add_node(graph, node)
            else:
                self.render_proc(graph, pname, subcluster)

    def render_target(self, graph: gvDigraph, name, cluster):
        """Renders a target cluster"""

        prefix = "cluster_" if config.TARGET_CLUSTERS else ""

        self.unique_id += 1
        with graph.subgraph(name=prefix+str(self.unique_id)) as tgraph:
            tgraph.attr(style="filled,solid", color=COLORS['target'],
                        fillcolor=COLORS['target_fill'])

            for pname, subcluster in cluster.items():
                if pname is None:
                    for node in subcluster:
                        self.add_node(tgraph, node)
                else:
                    self.render_proc(tgraph, pname, subcluster)

            tgraph.attr(label=name)

    def render_proc(self, graph: gvDigraph, name, cluster):
        """Renders a procedure cluster"""

        prefix = "cluster_" if config.PROC_CLUSTERS else ""

        self.unique_id += 1
        with graph.subgraph(name=prefix+str(self.unique_id)) as pgraph:
            pgraph.attr(style='solid,filled', color=COLORS['proc_arg'],
                        fillcolor=COLORS['proc_fill'])

            for node in cluster:
                self.add_node(pgraph, node)

            pgraph.attr(label=name)

    def add_node(self, graph: gvDigraph, node: Node):
        """Adds a node to graph, doesn't add edges"""
        color = COLORS[node.id_tuple[0]]
        fontcolor = 'white' if color == 'rebeccapurple' else 'black'
        label = node.id_tuple[-1]

        # Add the main node
        self.unique_id += 1
        node_id = f"node_{self.unique_id}"
        self.node_ids[node] = node_id

        self.unique_id += 1
        with graph.subgraph(name=f"cluster_{self.unique_id}") as ngraph:
            ngraph.attr(style="dotted", color=color)
            ngraph.node(
                node_id,
                f"{label} [{node.known_type}]",
                style="filled", color=color,
                fontcolor=fontcolor
            )

            # Add literal type nodes
            for type_ in self.frozen_types[node]:
                self.unique_id += 1
                ngraph.node(
                    f"type_{self.unique_id}",
                    str(type_),
                    style="filled", color=COLORS['type']
                )
                ngraph.edge(
                    f"type_{self.unique_id}",
                    node_id,
                )

    def render_edges(self, graph: gvDigraph):
        """Renders edges onto graph"""
        for node, parents in self.nodes.items():
            node_id = self.node_ids[node]

            # {node.id_tuple[-1]} [{node.known_type}]"
            # node_label = f"{node.id_tuple[-1]}"

            for parent in parents:
                # {parent.id_tuple[-1]} [{parent.known_type}]"
                parent_label = f"[{parent.known_type}]"

                parent_id = self.node_ids[parent]
                graph.edge(
                    parent_id, node_id,
                    # labeltooltip=f"{parent_label} to {node_label}",
                    headlabel=parent_label)  # , taillabel=node_label)
