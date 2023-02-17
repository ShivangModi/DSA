class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BSTIteration:
    def __init__(self, root=None):
        self.root = root
    
    def __insert(self, key):
        data = Node(key)
        if not self.root:   # is None
            self.root = data
            return
        
        parent = None
        root = self.root
        while root:
            if root.data == key:
                return
            parent = root
            if root.data > key:
                root = root.left
            else:
                root = root.right
        if parent.data > key:
            parent.left = data
        else:
            parent.right = data

    def arrayToBinaryTree(self, arr):
        for i in arr:
            self.__insert(i)
    
    def search(self, key):
        parent = None
        root = self.root
        while root:
            if root.data == key:
                if not parent:
                    print(f'The node with key {key} is root node')
                elif key < parent.data:
                    print(f'The given key {key} is the left node of {parent.data}')
                else:
                    print(f'The given key {key} is the right node of {parent.data}')
                return
            parent = root
            if root.data > key:
                root = root.left
            else:
                root = root.right
        if not root:
            print(f'Key {key} not found')
            return

    def __check(self, root):
        if not root:
            return -1
        
        left = self.__check(root.left)
        if left is False:
            return False

        right = self.__check(root.right)
        if right is False:
            return False

        if abs(left-right)>1:
            return False
        return max(left, right)+1
    
    def isBalanced(self):
        if self.__check(self.root) is not False:
            print("Tree is balanced")
        else:
            print("Tree is not balanced")

    def height(self, root):
        if not root:
            return -1
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r)+1

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=' ')
            self.printInorder(root.right)
            return

if __name__ == "__main__":
    arr = [8, 3, 1, 6, 7, 10, 14, 4]
    bst = BSTIteration()
    bst.arrayToBinaryTree(arr)
    bst.search(1)
    bst.search(8)
    bst.search(14)
    bst.search(2)
    bst.isBalanced()
    bst.printInorder(bst.root)