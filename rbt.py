RED = "RED"
BLACK = "BLACK"


class NilNode(object):
    def __init__(self):
        self.color = BLACK

"""We define NIL to be the leaf sentinel of our tree."""
NIL = NilNode()


class Node(object):
    def __init__(self, key, color=RED, left=NIL, right=NIL, p=NIL):
        """Constructs a single node of the red-black tree.
        Key is the key that has an ordering.
        color is RED or BLACK.
        left and right are the left and right subtrees.
        p is the parent Node.
        """
        assert color in (RED, BLACK)
        self.color, self.key, self.left, self.right, self.p = (
            color, key, left, right, p)


class Tree(object):
    def __init__(self, root=NIL):
        self.root = root

def left_rotate(T, x):
    """Left-rotates node x on tree T.

               x
              / \
             a   y
                / \
               b   g

    mutates into:

               y
              / \
             x   g
            / \
           a   b

    Used for maintaining tree balance.
    """
    assert (x.right != NIL)
    y = x.right
    x.right = y.left
    if y.left != NIL:
        y.left.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def right_rotate(T, x):
    """Right-rotates node x on tree T.

               x
              / \
             y   g
            / \
           a   b

    mutates into:

               y
              / \
             a   x
                / \
               b   g

    Used for maintaining tree balance.
    """
    assert (x.left != NIL)
    y = x.left
    x.left = y.right
    if y.right != NIL:
        y.right.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y

def tree_insert(tree, z):
    """Inserts node 'z' into binary tree 'tree'."""
    y = NIL
    x = tree.root
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == NIL:
        tree.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def rb_insert(tree, x):
    """Does an insertion of 'x' into the red-black tree 'tree'.  The
    algorithm here is a little subtle, but is explained in CLR."""
    tree_insert(tree, x)
    x.color = RED
    while x != tree.root and x.p.color == RED:
        if x.p == x.p.p.left:
            y = x.p.p.right
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.right:
                    x = x.p
                    left_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                right_rotate(tree, x.p.p)
        else:
            y = x.p.p.left
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.left:
                    x = x.p
                    right_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                left_rotate(tree, x.p.p)
    tree.root.color = BLACK

def preOrder(root):
    if root == NIL:
        return

    if root.p == NIL:
        print(root.key, root.color, root.p)
    else:
        print(root.key, root.color, root.p.key)

    preOrder(root.left)
    preOrder(root.right)

# rbt = Tree()
# rb_insert(rbt, Node(7))
# rb_insert(rbt, Node(3))
# rb_insert(rbt, Node(18))
# rb_insert(rbt, Node(10))
# rb_insert(rbt, Node(22))
# rb_insert(rbt, Node(8))
# rb_insert(rbt, Node(11))
# rb_insert(rbt, Node(26))

# print(rbt.root.key)
# preOrder(rbt.root)
# print('\n')
