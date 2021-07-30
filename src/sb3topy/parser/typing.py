"""
typing.py

Used to determine the type of variables and procedure arguments.

Makes a directed graph, where each node is a variable or argument.

Example Node id_tuples:
    ('var', 'sprite1', 'my variable')
    ('proc_arg', 'sprite1', 'custom block %s', 'x pos')


Valid types are:
    bool, int, float, str, any

"""

import logging

from graphviz import Digraph

from . import specmap

# Contains every possible combination of
# types and what the resulting type should be
RESOLVE_DICT = {
    # Single value
    frozenset(('bool',)): 'bool',
    frozenset(('int',)): 'int',
    frozenset(('float',)): 'float',
    frozenset(('str',)): 'str',
    frozenset(('any',)): 'any',

    # Single value + any
    frozenset(('bool', 'any')): 'any',
    frozenset(('int', 'any')): 'any',
    frozenset(('float', 'any')): 'any',
    frozenset(('str', 'any')): 'any',

    # Two values
    frozenset(('bool', 'int')): 'int',
    frozenset(('int', 'float')): 'float',
    frozenset(('float', 'str')): 'any',

    # Two values + any
    frozenset(('bool', 'int', 'any')): 'any',
    frozenset(('int', 'float', 'any')): 'any',
    frozenset(('float', 'str', 'any')): 'any',

    # Three values (+ any)
    frozenset(('bool', 'int', 'float')): 'float',
    frozenset(('bool', 'int', 'float', 'any')): 'any',

    # Four values (+ any)
    frozenset(('bool', 'int', 'float', 'str')): 'any',
    frozenset(('bool', 'int', 'float', 'str', 'any')): 'any',
}

NODE_COLORS = {
    'var': 'orange',
    'list': 'darkorange',
    'proc_arg': 'purple'
}


class Node:
    """
    Represents an item of a certain type

    id_tuple - A tuple providing unique identification for the node

    known_type - The known type of this node

    set_types - The types the item has been "set" to. Does not
        include the type of parent Nodes until they are resolved.

    parent_nodes - A set of nodes which this node is dependent on.

    nodes (class attribute) - A dict where the key is the
        id_tuple and the value is the corresponding node

    unresolved (class_attribute) - A set containing every unresolved node
    """

    nodes = {}
    unresolved = set()

    def __init__(self, id_tuple):
        self.id_tuple = id_tuple

        self.known_type = None

        self.set_types = set()
        # self.get_types = set()

        self.parent_nodes = set()

        self.nodes[id_tuple] = self
        self.unresolved.add(self)

    def __hash__(self):
        return hash(self.id_tuple)

    def add_type(self, set_type):
        """Notes that this item is set to a type"""
        # Check if the set_type is a node
        if isinstance(set_type, tuple):
            node = self.nodes[set_type]
            self.parent_nodes.add(node)

        # Otherwise, save the simple type
        else:
            self.set_types.add(set_type)

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


        return - Returns a set containing all the types this node is known to
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
                self.set_types.update(parent.resolve(chain, branch_loops))

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

        # Return set_types even if unresolved
        return self.set_types

    def force_resolve(self):
        """
        Forces the node to resolve based on its current set_types.

        Should only be called after all of the node's parents have resolved.
        """
        self.known_type = RESOLVE_DICT[frozenset(self.set_types)]
        self.unresolved.remove(self)

    @classmethod
    def resolve_all(cls):
        """Resolves all nodes"""
        while cls.unresolved:
            # TODO Temp render stuff
            cls.render()
            input("Press enter...")

            # Resolve an unresolved node
            next(iter(cls.unresolved)).resolve(set(), set())

    @classmethod
    def render(cls):
        """Draws a rendering of the directed graph"""

        dot = Digraph()
        for node in cls.nodes.values():
            dot.node(str(node.id_tuple), node.id_tuple[-1],
                     color=NODE_COLORS[node.id_tuple[0]])
            for parent in node.parent_nodes:
                dot.edge(str(parent.id_tuple), str(node.id_tuple))
                print(str(parent.id_tuple), str(node.id_tuple))

        dot.render(view=True)


def add_node(*id_tuple):
    """Creates a node from id data"""
    if id_tuple not in Node.nodes:
        logging.debug("Created type node %s", id_tuple)
        Node(id_tuple)
    else:
        logging.warning("Duplicate type node %s", id_tuple)


def mark_set(id_tuple, target, inp):
    """Marks a node as being set to an block input"""
    input_type = specmap.get_input_type(target, inp)

    if id_tuple not in Node.nodes:
        id_tuple = ('var', 'Stage', id_tuple[2])

    if input_type is not None:
        if isinstance(input_type, tuple):
            Node.nodes[id_tuple].parent_nodes.add(input_type)
        else:
            Node.nodes[id_tuple].set_types.add(input_type)


def mark_set_literal(id_tuple, value):
    """Marks a node as being set to a literal value"""
    if id_tuple not in Node.nodes:
        id_tuple = ('var', 'Stage', id_tuple[2])
    Node.nodes[id_tuple].set_types.add(specmap.get_type(value))
