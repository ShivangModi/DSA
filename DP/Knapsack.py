class Item:
    def __init__(self, weight=None, value=None):
        self.weight = weight
        self.value = value


class KnapsackProblem:
    def rec(self, arr, cap, n):
        if n==0 or cap==0:
            return 0
        if arr[n-1].weight > cap:
            return self.rec(arr, cap, n-1)
        else:
            return max(self.rec(arr, cap, n-1), self.rec(arr, cap-arr[n-1].weight, n-1) + arr[n-1].value)

    def memoization(self, arr, cap, n, k=None):
        if n==0 or cap==0:
            return 0

        if k is None:
            n = len(arr)
            k = list()
            for _ in range(n+1):
                k.append([-1]*(cap+1))
        
        if k[n][cap] != -1:
            return k[n][cap]
        
        if arr[n-1].weight <= cap:
            k[n][cap] = max(self.memoization(arr, cap, n-1, k), self.memoization(arr, cap-arr[n-1].weight, n-1, k) + arr[n-1].value)
            return k[n][cap]
        else:
            k[n][cap] = self.memoization(arr, cap, n-1, k)
            return k[n][cap]

    def dp(self, arr, cap):
        n = len(arr)
        k = list()
        for _ in range(n+1):
            k.append([0]*(cap+1))
        arr.sort(key = lambda x: x.weight)

        for i in range(n+1):
            for w in range(cap+1):
                if i == 0 or w == 0:
                    k[i][w] = 0
                elif arr[i-1].weight <= w:
                    k[i][w] = max(k[i-1][w], k[i-1][w-arr[i-1].weight] + arr[i-1].value)
                else:
                    k[i][w] = k[i-1][w]
        
        return k[n][cap]
        

if __name__ == "__main__":
    arr = list()
    arr.append(Item(2, 10))
    arr.append(Item(3, 5))
    arr.append(Item(5, 15))
    arr.append(Item(7, 7))
    arr.append(Item(1, 6))
    arr.append(Item(4, 18))
    arr.append(Item(1, 3))

    # arr = list()
    # arr.append(Item(10, 60))
    # arr.append(Item(20, 100))
    # arr.append(Item(30, 120))

    capacity = 10
    ks = KnapsackProblem()
    print(ks.rec(arr, capacity, len(arr)))
    print(ks.memoization(arr, capacity, len(arr)))
    print(ks.dp(arr, capacity))