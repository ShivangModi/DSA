class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.__head = head
    
    def isEmpty(self):
        return self.__head is None
    
    def push(self, val):
        new = Node(val)
        if self.isEmpty():
            self.__head = new
            return
        new.next = self.__head
        self.__head = new
    
    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            temp = self.__head
            self.__head = self.__head.next
            temp.next = None
            return temp
    
    def peek(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.__head.data
    
    def display(self):
        if self.isEmpty():
            print("Underflow")
        else:
            temp = self.__head
            while temp is not None:
                print(f"{temp.data} ->", end=" ")
                temp = temp.next
            print()
            return
