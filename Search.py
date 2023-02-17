# Linear Search Algorithm:-
# Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, 
# otherwise the search continues till the end of the data set. It is the easiest searching algorithm.
# The time complexity of the Linear search is O(n).

# Problem:- Iterate from 0 to N-1 and compare the value of every index with x if they match return index and If x doesn’t match with any of the elements, return -1.    
class Search:
    def __init__(self, arr):
        self.arr = arr

    def LinearSearch(self, val):
        for i in range(len(self.arr)):
            if self.arr[i] == val:
                return i
        return -1   #   Element is not present


    # Binary Search Algorithm:-
    # Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
    # The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).

    # Steps:-
    # 1. Begin with the mid element of the whole array as a search key.
    # 2. If the value of the search key is equal to the item then return an index of the search key.
    # 3. Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
    # 4. Otherwise, narrow it to the upper half.
    # 5. Repeatedly check from the second point until the value is found or the interval is empty.

    # Binary Search Algorithm can be implemented in the following two ways
    # 1. Iterative Method
    # 2. Recursive Method

    # Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[] and return the index of x in the array.

    # Iterative Method
    def BinarySearch(self, val):
        low = 0
        high = len(self.arr) - 1
        while low<=high:
            mid = (low+high)//2
            if self.arr[mid] == val:
                return mid
            elif self.arr[mid] > val:
                high = mid-1
            else:
                low = mid+1
        return -1

    # Recursive Method
    def BinarySearch(self, val, low, high):
        if low > high:
            return -1   #   Element is not present
        mid = (low+high)//2
        if self.arr[mid] == val:
            return mid
        elif self.arr[mid] > val:
            return self.BinarySearch(val, low, mid-1)
        else:
            return self.BinarySearch(val, mid+1, high)