class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BSTRecursion:
    def __init__(self, root=None):
        self.root = root
    
    def __insert(self, root, key):
        if not root:    # is None
            return Node(key)
        if root.data > key:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)
        return root

    def arrayToBinaryTree(self, arr):
        for i in arr:
            self.root = self.__insert(self.root, i)
    
    def search(self, key, root, parent=None):
        if not root:    # is None
            print(f'Key {key} not found')
            return
        if root.data == key:
            if not parent:  # is None
                print(f'The node with key {key} is root node')
            elif key < parent.data:
                print(f'The given key {key} is the left node of {parent.data}')
            else:
                print(f'The given key {key} is the right node of {parent.data}')
            return
        if key < root.data:
            self.search(key, root.left, root)
        else:
            self.search(key, root.right, root)
    
    def __check(self, root):
        if not root:    # is None
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
        if self.__check(self.root) != False:
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

if __name__ == "__main__":
    arr = [8, 3, 1, 6, 7, 10, 14, 4]
    bst = BSTRecursion()
    bst.arrayToBinaryTree(arr)
    bst.search(1, bst.root)
    bst.search(8, bst.root)
    bst.search(14, bst.root)
    bst.search(2, bst.root)
    bst.isBalanced()
    bst.printInorder(bst.root)