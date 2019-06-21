def complete_binary_tree(a):
    pass


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
