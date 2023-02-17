class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularQueue:
    def __init__(self, front=None, rear=None):
        self.__front = front
        self.__rear = rear
    
    def enqueue(self, val):
        new = Node(val)
        if not self.__front:
            self.__rear = self.__front = new
            return
        self.__rear.next = new
        self.__rear = new
        self.__rear.next = self.__front
    
    def dequeue(self):
        if not self.__front:
            print("Queue is Empty")
            return
        if self.__front == self.__rear:
            self.__front = self.__rear = None
            return
        self.__front = self.__front.next
        self.__rear.next = self.__front
    
    def display(self):
        temp = self.__front
        while temp.next != self.__front:
            print(temp.data, end=' ')
            temp = temp.next
        print(temp.data)