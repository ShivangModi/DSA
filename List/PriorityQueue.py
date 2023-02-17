# Priority Queue:-
# Priority Queue is an abstract data type that is similar to a queue, and every element has some priority value associated with it. 
# The priority of the elements in a priority queue determines the order in which elements are served (i.e., the order in which they are removed). 
# If in any case the elements have same priority, they are served as per their ordering in the queue.
# Therefore all the elements are either arranged in an ascending or descending order.

# Properties of Priority Queue:-
# A priority Queue is an extension of the queue with the following properties: 
#   - Every item has a priority associated with it.
#   - An element with high priority is dequeued before an element with low priority.
#   - If two elements have the same priority, they are served according to their order in the queue.

# How is Priority assigned to the elements in a Priority Queue?
# In a priority queue, generally, the value of an element is considered for assigning the priority. 
# For example, the element with the highest value is assigned the highest priority and the element with the lowest value is assigned the lowest priority. 
# The reverse case can also be used i.e., the element with the lowest value can be assigned the highest priority. 
# Also, the priority can be assigned according to our needs.

# Operations of a Priority Queue:-
# A typical priority queue supports the following operations:
#   1) Insertion in a Priority Queue: 
#      When a new element is inserted in a priority queue, it moves to the empty slot from top to bottom and left to right. 
#      However, if the element is not in the correct place then it will be compared with the parent node. 
#      If the element is not in the correct order, the elements are swapped. 
#      The swapping process continues until all the elements are placed in the correct position.
#   2) Deletion in a Priority Queue:
#      As you know that in a max heap, the maximum element is the root node. And it will remove the element which has maximum priority first. 
#      Thus, you remove the root node from the queue. This removal creates an empty slot, which will be further filled with new insertion. 
#      Then, it compares the newly inserted element with all the elements inside the queue to maintain the heap invariant.
#   3) Peek in a Priority Queue
#      This operation helps to return the maximum element from Max Heap or the minimum element from Min Heap without deleting the node from the priority queue.

# Types of Priority Queue:-
#   1) Ascending Order Priority Queue:
#      As the name suggests, in ascending order priority queue, the element with a lower priority value is given a higher priority in the priority list. 
#      For example, if we have the following elements in a priority queue arranged in ascending order like 4,6,8,9,10. Here, 4 is the smallest number, therefore, it will get the highest priority in a priority queue.
#   2) Descending order Priority Queue:
#      The root node is the maximum element in a max heap, as you may know. It will also remove the element with the highest priority first. 
#      As a result, the root node is removed from the queue. This deletion leaves an empty space, which will be filled with fresh insertions in the future. 
#      The heap invariant is then maintained by comparing the newly inserted element to all other entries in the queue.

# Difference between Priority Queue and Normal Queue?
# There is no priority attached to elements in a queue, the rule of first-in-first-out(FIFO) is implemented whereas, in a priority queue, the elements have a priority. 
# The elements with higher priority are served first.

# How to Implement Priority Queue? 
# Priority queue can be implemented using the following data structures: 
#   - Arrays
#   - Linked list
#   - Heap data structure
#   - Binary search tree
class item:
    def __init__(self, val, priority):
        self.value = val
        self.priority = priority


# Note:-
# Assume that Priority 0 indicates the highest Priority and M is the lowest
class PriorityQueue:
    def __init__(self):
        self.__size = 10 ** 5
        self.__data = [None] * self.__size
        self.__head = 0
        self.__tail = 0

    # Insertion Sort
    def __sort(self):
        for i in range(1, self.__tail):
            key = self.__data[i]
            j = i - 1
            while j >= self.__head and self.__data[j].priority > key.priority:
                self.__data[j + 1] = self.__data[j]
                j -= 1
            self.__data[j + 1] = key

    def isEmpty(self):
        return self.__tail == self.__head

    def isFull(self):
        return self.__tail == self.__size

    def enqueue(self, val, priority):
        if self.isFull():
            print("Overflow")
            return
        self.__data[self.__tail] = item(val, priority)

        # insertion sort
        key = self.__data[self.__tail]
        j = self.__tail - 1
        while j >= self.__head and self.__data[j].priority > key.priority:
            self.__data[j + 1] = self.__data[j]
            j -= 1
        self.__data[j + 1] = key

        self.__tail += 1

    def dequeue(self):
        if self.isEmpty():
            self.__head = self.__tail = 0
            print("Underflow")
            return
        else:
            res = self.__data[self.__head]
            self.__data[self.__head] = None
            self.__head += 1
            return res

    def changePriority(self, val, priority):
        flag = False
        for i in range(self.__head, self.__tail):
            if self.__data[i].value == val:
                self.__data[i].priority = priority
                flag = True
        if not flag:
            print(f"Priority Queue doesn't have value={val}\n")
            return
        self.__sort()

    def display(self):
        for i in range(self.__head, self.__tail):
            print(self.__data[i].value, self.__data[i].priority)
        print()


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(10, 5)
    pq.enqueue(20, 3)
    pq.enqueue(30, 3)
    pq.enqueue(40, 2)
    pq.enqueue(50, 1)
    pq.display()
    pq.dequeue()
    pq.changePriority(30, 0)
    pq.changePriority(60, 0)
    pq.display()
