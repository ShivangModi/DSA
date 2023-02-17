# Linked List:-
# Like arrays, Linked List is a linear data structure. 
# Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers. 
# They include a series of connected nodes. 
# Here, each node stores the data and the address of the next node.

# Why Linked List? 
# Arrays can be used to store linear data of similar types, but arrays have the following limitations:
#   - The size of the arrays is fixed: 
#     So we must know the upper limit on the number of elements in advance. 
#     Also, generally, the allocated memory is equal to the upper limit irrespective of the usage. 
#   - Insertion of a new element / Deletion of a existing element in an array of elements is expensive: 
#     The room has to be created for the new elements and to create room existing elements have to be shifted.
#     but in Linked list if we have the head node then we can traverse to any node through it and insert new node at the required position.

# Example:- 
# In a system, if we maintain a sorted list of IDs in an array id[] = [1000, 1010, 1050, 2000, 2040]. 
# If we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000). 
# Deletion is also expensive with arrays until unless some special techniques are used. 
# For example, to delete 1010 in id[], everything after 1010 has to be moved due to this so much work is being done which affects the efficiency of the code.

# Advantages of Linked Lists over arrays:-
#   - Dynamic Array.
#   - Ease of Insertion/Deletion.

# Drawbacks of Linked Lists:-
#   - Random access is not allowed. We have to access elements sequentially starting from the first node(head node). 
#     So we cannot do a binary search with linked lists efficiently with its default implementation. 
#   - Extra memory space for a pointer is required with each element of the list. 
#   - Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

# Types of Linked Lists:-
#   - Simple Linked List: 
#     In this type of linked list, one can move or traverse the linked list in only one direction
#   - Doubly Linked List:
#     In this type of linked list, one can move or traverse the linked list in both directions (Forward and Backward)
#   - Circular Linked List: 
#     In this type of linked list, the last node of the linked list contains the link of the first/head node of the linked list in its next pointer and 
#     the first/head node contains the link of the last node of the linked list in its prev pointer

# Basic operations on Linked Lists:-
#   - Deletion
#   - Insertion
#   - Search
#   - Display

# Representation of Linked Lists:-
# A linked list is represented by a pointer to the first node of the linked list. 
# The first node is called the head of the linked list. 
# If the linked list is empty, then the value of the head points to NULL. 
# Each node in a list consists of at least two parts: 
#   - A Data Item (we can store integer, strings, or any type of data).
#   - Pointer (Or Reference) to the next node (connects one node to another) or An address of another node

import gc

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class SimpleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertFront(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def insertAfter(self, prev, data):
        # check if the given prev node exists
        if not prev:
            print("Previous node can't be None")
            return
        new = Node(data)
        new.next = prev.next
        prev.next = new
    
    def insertEnd(self, data):
        new = Node(data)
        # If the Linked List is empty, then make the new node as head
        if not self.head:
            self.head = new
            return
        # Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new
    
    def deleteFront(self):
        if not self.head:
            print("Underflow")
            return
        first = self.head
        self.head = self.head.next
        del first
    
    def deleteEnd(self):
        if not self.head:
            print("Underflow")
            return
        if not self.head.next:
            self.head = None
            return
        sec_last = self.head
        while sec_last.next.next:
            sec_last = sec_last.next
        last = sec_last.next
        sec_last.next = None
        del last
    
    def reverse(self):
        rev = None
        current = self.head
        while current:
            next = current.next
            current.next = rev
            rev = current
            current = next
        self.head = rev

    def search(self, key):
        start = self.head
        while start:
            if start.data == key:
                return True
            start = start.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp)


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertFront(self, data):
        new = Node(data)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new
    
    def insertAfter(self, pre, data):
        # check if the given prev node exists
        if not pre:
            print("Previous node can't be None")
            return
        new = Node(data)
        new.next = pre.next
        pre.next = new
        new.prev = pre
        if new.next:
            new.next.prev = new
    
    def insertEnd(self, data):
        new = Node(data)
        # If the Linked List is empty, then make the new node as head
        if not self.head:
            self.head = new
            return
        # Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new
        new.prev = last
    
    def deleteFront(self):
        if not self.head:
            print("Underflow")
            return
        first = self.head
        self.head = self.head.next
        self.head.prev = None
        del first
    
    def deleteNode(self, dele):
        if not (self.head or dele):
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next:
            dele.next.prev = dele.prev
        if dele.prev:
            dele.prev.next = dele.next
        # Free the memory of deleted node
        gc.collect()
    
    def deleteEnd(self):
        if not self.head:
            print("Underflow")
            return
        if not self.head.next:
            self.head = None
            return
        sec_last = self.head
        while sec_last.next.next:
            sec_last = sec_last.next
        last = sec_last.next
        sec_last.next = None
        del last

    def display(self):
        temp = self.head
        print(temp.prev, end=" <-> ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(temp)


class CircularLinkedList:
    def __init__(self, tail=None):
        self.tail = tail
    
    def __insertEmpty(self, new):
        self.tail = new
        self.tail.next = new

    def insertFront(self, data):
        new = Node(data)
        if self.tail is None:
            self.__insertEmpty(new)
            return
        new.next = self.tail.next
        self.tail.next = new
    
    def insertEnd(self, data):
        new = Node(data)
        # If the Linked List is empty, then make the new node as head
        if self.tail is None:
            self.__insertEmpty(new)
            return
        new.next = self.tail.next
        self.tail.next = new
        self.tail = new
    
    def deleteFront(self):
        if self.tail is None:
            print("Underflow")
            return
        if self.tail.next == self.tail:
            self.tail = None
            return
        self.tail.next = self.tail.next.next
        gc.collect()
    
    def deleteEnd(self):
        if self.tail is None:
            print("Underflow")
            return
        if self.tail.next == self.tail:
            self.tail = None
            return
        sec_last = self.tail.next
        while sec_last.next != self.tail:
            sec_last = sec_last.next
        sec_last.next = self.tail.next
        self.tail = sec_last
        gc.collect()

    def display(self):
        temp = self.head
        print(temp.prev, end=" <-> ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(temp)

if __name__ == "__main__":
    l = DoublyLinkedList()
    l.insertEnd(1)
    l.insertEnd(2)
    l.insertEnd(3)
    l.insertEnd(4)
    l.insertEnd(5)
    l.display()
    # l.reverse()
    # l.display()