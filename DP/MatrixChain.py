from sys import maxsize


class MatrixChain:
    def rec(self, arr, i, j):
        if i == j:
            return 0

        _min = maxsize
        for k in range(i, j):
            count = self.rec(arr, i, k) + self.rec(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
            if count < _min:
                _min = count
        return _min

    def memoization(self, arr, i, j, dp=None):
        if i == j:
            return 0

        if dp is None:
            n = len(arr)
            dp = list()
            for _ in range(n):
                dp.append([maxsize] * n)

        if dp[i][j] != maxsize:
            return dp[i][j]

        for k in range(i, j):
            dp[i][j] = min(dp[i][j],
                           self.memoization(arr, i, k, dp) + self.memoization(arr, k + 1, j, dp) + arr[i - 1] * arr[k] *
                           arr[j])
        return dp[i][j]

    def dp(self, arr, n):
        dp = list()
        for i in range(n):
            dp.append([maxsize] * n)
            dp[i][i] = 0

        for l in range(2, n):
            for i in range(1, n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j])
        return dp[1][n - 1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 3]
    n = len(arr)

    mc = MatrixChain()
    print(mc.rec(arr, 1, n - 1))
    print(mc.memoization(arr, 1, n - 1))
    print(mc.dp(arr, n))
    pass
