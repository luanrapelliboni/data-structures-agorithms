from lib2to3.pgen2.literals import simple_escapes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        
        print(node, end='')

        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
    
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.inorder_traversal(node.left)
        
        print(node, end=' ')

        if node.right:
            self.inorder_traversal(node.right)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
        
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

if __name__ == "__main__":
    #           '+'
    #         /     \
    #       'a'     '*'
    #              /   \
    #            'b'    '-'
    #                  /   \
    #                '/'    'e'
    #               /   \
    #             'c'   'd'      
    #   (c/d)
    # tree = BinaryTree()
    # n1 = Node('a')
    # n2 = Node('+')
    # n3 = Node('*')
    # n4 = Node('b')
    # n5 = Node('-')
    # n6 = Node('/')
    # n7 = Node('c')
    # n8 = Node('d')
    # n9 = Node('e')

    # n6.left = n7
    # n6.right = n8
    # n5.left = n6
    # n5.right = n9
    # n3.left = n4 
    # n3.right = n5
    # n2.left = n1
    # n2.right = n3
    # tree.root = n2

    # tree.simetric_traversal()
    # print('')

    #print(tree.height())


    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)

    #tree.inorder_traversal()    
    item = 100
    r = tree.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, 'encontrado')