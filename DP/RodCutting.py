class RodCutting:
    def rec(self, rodPrice, length, index):
        if index == 0:
            return length * rodPrice[index]
        
        notCut = self.rec(rodPrice, length, index-1)
        cut = float('-inf')

        rod_len = index+1
        if rod_len <= length:
            cut = rodPrice[index] + self.rec(rodPrice, length - rod_len, index)
        return max(notCut, cut)

    def memoization(self, rodPrice, length, index, dp=None):
        if index == 0:
            return length * rodPrice[index]
        
        if dp is None:
            dp = list()
            for _ in range(length):
                dp.append([-1]*(length+1))
        
        if dp[index][length] != -1:
            return dp[index][length]
        
        notCut = self.memoization(rodPrice, length, index-1, dp)
        cut = float('-inf')

        rod_len = index+1
        if rod_len <= length:
            cut = rodPrice[index] + self.memoization(rodPrice, length - rod_len, index, dp)
        dp[index][length] = max(notCut, cut)
        return dp[index][length]

    def dp(self, rodPrice, n):
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == 1:
                    dp[i][j] = j*rodPrice[i-1]
                else:
                    if i > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], rodPrice[i-1] + dp[i][j-i])
        return dp[n][n]


if __name__ == "__main__":
    rodPrice = [1, 5, 8, 9, 10, 17, 17, 20]
    length = len(rodPrice)
    rc = RodCutting()
    print(rc.rec(rodPrice, length, length-1))
    print(rc.memoization(rodPrice, length, length-1))
    print(rc.dp(rodPrice, length))