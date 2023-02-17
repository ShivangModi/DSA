# Implement the Linked List with the following functions:
#   a. Function to return the number of elements with O(1) complexity
#      Linked list to be printed 
#   b. Function to print the last element with O(1) complexity
#   c. Function to enqueue front with O(1) complexity
#      Linked list to be printed 
#   d. Function to remove the even elements (refers the positions) with O(n/2) complexity

class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, head=None):
        self.head = head
        self.__last = None #   last element of linked list O(1) complexity
        self.__len = 0

    def insert(self, data):
        new = self.Node(data)
        if not self.head:
            self.__last = new
        new.next = self.head
        self.head = new
        self.__len += 1
        self.__print()
    
    def remove(self):
        temp = self.head
        while temp.next:
            n = temp.next
            if n.next is None:
                temp.next = None
                self.__last = temp
                break
            temp.next = n.next
            temp = temp.next
        self.__len -= self.__len//2
        self.__print()
    
    def length(self):
        return self.__len
    
    def printlast(self):
        return self.__last.data

    def __print(self):
        if not self.length():
            print ("List Empty")
        else:
            tnode = self.head
            while tnode:
                print(tnode.data, end="->")
                tnode = tnode.next
            print("null")
        return

if __name__ == "__main__":
    l = LinkedList()
    l.insert("1")
    l.insert("2")
    l.insert("3")
    l.insert("4")
    print(l.length())
    print(l.printlast())
    l.remove()
    print(l.length())
    l.remove()
    print(l.length())
    