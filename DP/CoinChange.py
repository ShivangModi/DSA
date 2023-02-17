import sys


class CoinChange:
    def rec(self, coins, change, n):
        if change == 0:
            return 0

        res = sys.maxsize
        for i in range(n):
            if coins[i] <= change:
                temp = self.rec(coins, change - coins[i], n)
                if temp != sys.maxsize and temp + 1 < res:
                    res = temp + 1
        return res

    def memoization(self, coins, change, n, table=None):
        if change == 0:
            return 0

        if table is None:
            table = [sys.maxsize for _ in range(change + 1)]

        if table[n] != sys.maxsize:
            return table[change]

        for i in range(n):
            if coins[i] <= change:
                temp = self.memoization(coins, change - coins[i], n, table)
                if temp != sys.maxsize and temp + 1 < table[change]:
                    table[change] = temp + 1
        return table[change]

    def dp(self, coins, change, n):
        table = [sys.maxsize for _ in range(change + 1)]

        # Base case if change is 0
        table[0] = 0

        for i in range(1, change + 1):
            for j in range(n):
                temp = table[i - coins[j]]
                if temp != sys.maxsize and temp + 1 < table[i]:
                    table[i] = temp + 1

        if table[change] == sys.maxsize:
            return -1
        return table[change]


if __name__ == "__main__":
    coins = [1, 2, 5]
    change = 8
    ccc = CoinChange()
    print(ccc.rec(coins, change, len(coins)))
    print(ccc.memoization(coins, change, len(coins)))
    print(ccc.dp(coins, change, len(coins)))
