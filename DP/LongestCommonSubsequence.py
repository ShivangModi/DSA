class LCS:
    def rec(self, x, y, m, n):
        if m == 0 or n == 0:
            return 0
        elif x[m-1] == y[n-1]:
            return 1 + self.rec(x, y, m-1, n-1)
        else:
            return max(self.rec(x, y, m, n-1), self.rec(x, y, m-1, n))

    def memoization(self, x, y, m, n, dp=None):
        if m == 0 or n == 0:
            return 0
        
        if dp is None:
            dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        if dp[m][n] != -1:
            return dp[m][n]

        if x[m-1] == y[n-1]:
            dp[m][n] = 1 + self.memoization(x, y, m-1, n-1, dp)
            return dp[m][n]
        
        dp[m][n] = max(self.memoization(x, y, m, n-1), self.memoization(x, y, m-1, n))
        return dp[m][n]

    def dp(self, x, y, m, n):
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
        

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    m = len(x)
    n = len(y)

    lcs = LCS()
    print(lcs.rec(x, y, m, n))
    print(lcs.memoization(x, y, m, n))
    print(lcs.dp(x, y, m, n))