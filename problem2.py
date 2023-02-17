class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BT:
    def __init__(self, root=None):
        self.root = root
        self.sub = None

    def __insert(self, root, key):
        if not root:
            return Node(key)
        if root.data == key:
            return root
        elif root.data > key:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)
        return root

    def arrayToBinaryTree(self, arr):
        for i in arr:
            self.root = self.__insert(self.root, i)

    def __search(self, key, root, parent=None):
        temp = None
        if not root:
            return root
        if root.left.data == key:
            self.sub = root.left
            root.left = None
            return
        if root.right.data == key:
            self.sub = root.right
            root.right = None
            return
        if key < root.data:
            self.__search(key, root.left, root)
        else:
            self.__search(key, root.right, root)

    def subTree(self, key):
        root = self.root
        self.__search(key, root)
        print("Subtree1:")
        self.printInorder(self.root)
        print()
        print("Subtree2:")
        self.printInorder(self.sub)
        print()

    def depthOfLeaf(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [{"data": root.data, "depth": 0}]
        l = []
        l.extend(self.depthOfLeaf(root.left))
        l.extend(self.depthOfLeaf(root.right))
        for i in l:
            i["depth"] += 1
        return l

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=' ')
            self.printInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.data, end=' ')


if __name__ == "__main__":
    arr = [8, 3, 1, 6, 7, 10, 14, 4]
    bt = BT()
    bt.arrayToBinaryTree(arr)
    print(bt.depthOfLeaf(bt.root))
    print("Postorder:")
    bt.printPostorder(bt.root)
    print()
    bt.subTree(3)
