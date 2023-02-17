class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, val):
        new = Node(val)
        if self.rear is None:
            self.rear = self.front = new
            return
        self.rear.next = new
        self.rear = new
    
    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
        else:
            temp = self.front
            self.front = self.front.next
            del temp
            if self.isEmpty():
                self.rear = None


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front : " + str(q.front.data))
    print("Queue Rear : " + str(q.rear.data))