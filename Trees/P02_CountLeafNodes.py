# Author: OMKAR PATHAK

# leaf node is the one which does not have any children

class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    # for setting left node
    def setLeft(self, node):
        self.left = node

    # for setting right node
    def setRight(self, node):
        self.right = node

    # for getting the left node
    def getLeft(self):
        return self.left

    # for getting right node
    def getRight(self):
        return self.right

    # for setting data of a node
    def setData(self, data):
        self.data = data

    # for getting data of a node
    def getData(self):
        return self.data


def countLeafNodes(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(3))
    root.left.setLeft(Node(4))

    print('Count of leaf nodes:',countLeafNodes(root))
