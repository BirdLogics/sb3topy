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

from .. import config
from . import specmap


TYPE_COLORS = {
    'var': 'orange',
    'list': 'darkorange',
    'proc_arg': 'purple'
}


class Node:
    """
    Represents an item of a certain type

    id_tuple - A tuple providing unique identification for the node

    known_type - The known type of this node

    types_set - The types the item has been "set" to. Does not
        include the type of parent Nodes until they are resolved.

    parent_nodes - A set of nodes which this node is dependent on.

    unresolved - A set which this node adds and removes
        itself from depending on the unresolved status
    """

    def __init__(self, id_tuple, unresolved):
        self.id_tuple = id_tuple

        self.unresolved = unresolved
        self.unresolved.add(self)

        self.known_type = None

        self.types_set = set()
        # self.get_types = set()

        self.parent_nodes = set()

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
        """

        # Add self to chain to detect loops
        chain.add(self)

        # Get a set of all types this node can be
        for parent in self.parent_nodes:
            # Don't resolve a loop
            if parent in chain:
                loops.add(parent)

            # Resolve the parent
            else:
                # Loops don't matter for each parent's branch
                branch_loops = set()

                # Resolve the parent
                self.types_set.update(parent.resolve(chain, branch_loops))

                # Remove the parent if it has resolved
                if parent.known_type is not None:
                    self.parent_nodes.remove(parent)

                # Loops in the parent do matter for this branch
                loops.update(branch_loops)

        # Cannot resolve unless either loops is
        # empty or self is the only node in loops
        if not loops or len(loops) == 1 and self in loops:
            self.force_resolve()

        # Remove self from chain
        chain.remove(self)

        # Return types_set even if unresolved
        return self.types_set

    def force_resolve(self):
        """
        Forces the node to resolve based on its current types_set.

        Should only be called after all of the node's parents have resolved.
        """
        self.known_type = self.resolve_type(self.types_set.copy())
        self.unresolved.remove(self)

        logging.debug("Resolved %s type node '%s' as '%s'",
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
            logging.warning("Failed to identify type of '%s'", types_set)

        return 'any'


class DiGraph:
    """
    A directed graph used to determine types.

    nodes - A dict referencing nodes by their id_tuple

    unresolved - A set containing all unresolved nodesF
    """

    def __init__(self):
        self.nodes = {}
        self.unresolved = set()

    def add_node(self, id_tuple):
        """Creates a node from id data"""
        # Verify the node hasn't been created
        if id_tuple not in self.nodes:
            logging.debug("Creating type node %s", id_tuple)
            self.nodes[id_tuple] = Node(id_tuple, self.unresolved)

        else:
            logging.warning("Duplicate type node %s", id_tuple)

        return self.nodes[id_tuple]

    def resolve(self):
        """Resolves all nodes"""
        while self.unresolved:
            # Get and resolve an unresolved node
            next(iter(self.unresolved)).resolve(set(), set())

    # @classmethod
    # def render(cls):
    #     """Draws a rendering of the directed graph"""
    #     from graphviz import Digraph

    #     dot = Digraph()
    #     for node in cls.nodes.values():
    #         dot.node(str(node.id_tuple), node.id_tuple[-1],
    #                  color=NODE_COLORS[node.id_tuple[0]])
    #         for parent in node.parent_nodes:
    #             dot.edge(str(parent.id_tuple), str(node.id_tuple))
    #             print(str(parent.id_tuple), str(node.id_tuple))

    #     dot.render(view=True)
