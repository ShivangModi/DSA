class CoinChangeCombination:
    def __init__(self):
        self.arr = None

    def rec(self, coins, change, n):
        if change == 0:
            return 1
        
        if change < 0 or n <= 0:
            return 0
        
        return self.rec(coins, change, n-1) + self.rec(coins, change-coins[n-1], n)

    def memoization(self, coins, change, n):
        if change == 0:
            return 1
        
        if change < 0 or n <= 0:
            return 0
        
        if self.arr is None:
            self.arr = list()
            for _ in range(n+1):
                self.arr.append([-1]*(change+1))
        
        if self.arr[n][change] != -1:
            return self.arr[n][change]
        
        if coins[n-1] <= change:
            self.arr[n][change] = self.memoization(coins, change, n-1) + self.memoization(coins, change-coins[n-1], n)
            return self.arr[n][change]
        else:
            self.arr[n][change] = self.memoization(coins, change, n-1)
            return self.arr[n][change]

    def dp(self, coins, change, n):
        cc = list()
        for _ in range(n+1):
            cc.append([0]*(change+1))
        coins.sort()
        
        cc[0][0] = 1
        for j in range(1,change+1):
            cc[0][j] = 0
        
        for i in range(1, n+1):
            for coin in range(change+1):
                if coins[i-1] <= coin:
                    cc[i][coin] = cc[i-1][coin] + cc[i][coin-coins[i-1]]
                else:
                    cc[i][coin] = cc[i-1][coin]
        
        return cc[n][change] 


if __name__ == "__main__":
    coins = [1, 2, 5]
    change = 5
    ccc = CoinChangeCombination()
    print(ccc.rec(coins, change, len(coins)))
    print(ccc.memoization(coins, change, len(coins)))
    print(ccc.dp(coins, change, len(coins)))