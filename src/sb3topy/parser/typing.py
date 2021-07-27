"""
typing.py

Determines the type of variables and procedure arguments.


Valid types are:
    bool, int, float, str, any

"""

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


class Node:
    """
    Represents an item of a certain type

    id_tuple - A tuple providing unique identification
        for the item, eg. ('sprite1', 'var', 'my variable') or
        ('sprite1', 'proc_arg', 'custom block %s', 'x pos')

    guessed_type - The best guess as to the type of this item
    is_resolved - Whether the guessed type is final

    set_types - The types the item has been "set" to. Does not
        include the type of parent Nodes until they are resolved.

    child_nodes - A set of nodes which are dependent on
        the type of this node. If the type of this node is determined,
        the child nodes will be notified so they can update their type.

    parent_nodes - A set of nodes which this node is dependent on.

    nodes (class attribute) - A dict where the key is the number of
        parents and the value is a set of nodes with that many parents.

    nodes_all (class_attribute) - A list of every node
    """

    nodes = {}
    nodes_all = []

    def __init__(self, id_tuple):
        self.id_tuple = id_tuple

        self.guessed_type = None

        self.set_types = set()
        # self.get_types = set()

        self.parent_nodes = set()
        self.child_nodes = set()

        self.nodes_all.append(self)

    def __hash__(self):
        return hash(self.id_tuple)

    def add_type(self, set_type):
        """Notes that this item is set to a type"""
        # Check if the set_type is a node
        if isinstance(set_type, tuple):
            node = self.nodes[set_type]
            self.parent_nodes.add(node)
            node.child_nodes.add(self)

        # Otherwise, save the simple type
        else:
            self.set_types.add(set_type)

    def resolve(self):
        """
        Forcibly resolves the type of this node
        """
        # Remove self from parents' child sets
        for parent in self.parent_nodes:
            parent.child_nodes.pop(self)

        # Guess the type using RESOLVE_DICT and set_types
        self.guessed_type = RESOLVE_DICT[frozenset(self.set_types)]

        # Notify each child a parent node has resolved
        # Also get the child with the least number of parents

        return min(child.parent_resolved(self) for child in self.child_nodes)

    def parent_resolved(self, parent):
        """Called when a parent node resolves its type"""
        # Remove self from nodes
        parents = len(self.parent_nodes)
        self.nodes[parents].remove(self)

        # Save the type of the parent
        self.parent_nodes.remove(parent)
        self.set_types.add(parent.guessed_type)

        # Add self back to nodes in order
        self.nodes.setdefault(parents - 1, set()).add(self)

        # Return the new number of parents
        return parents - 1

    @classmethod
    def resolve_all(cls):
        """Resolves all nodes in the right order"""
        # TODO Is there a better order to resolve?
        # Would it be better to resolve in the order of
        # 1) least parents, and 2) most children?

        # Initialize the cls.nodes dict from cls.nodes_all
        # The key is the number of parents, and the value is
        # a set with all nodes that have that many parents
        for node in cls.nodes_all:
            cls.nodes.setdefault(len(node.parent_nodes), set()).add(node)

        parents = 0
        while cls.nodes:
            # Verify there is a set with a node in it
            if cls.nodes.get(parents):
                # Get a node with parents number of parent_nodes
                node = cls.nodes[parents].pop()

                # Resolve the node and update the parents count
                parents = min(parents, node.resolve())

            # Either there is a not a set or there is an empty one
            else:
                parents += 1
