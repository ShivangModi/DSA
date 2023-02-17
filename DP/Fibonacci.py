class Fibonacci:
    def __init__(self):
        self.term = [0]*1000

    def fib_rec(self, n):
        if n <= 1:
            return n
        return self.fib_rec(n-1) + self.fib_rec(n-2)

    def fib_memoization(self, n):
        if n <= 1:
            return n
        if self.term[n] != 0:
            return self.term[n]
        else:
            self.term[n] = self.fib_memoization(n-1) + self.fib_memoization(n-2)
            return self.term[n]   

    def fib_dp(self, n):
        term = [0, 1]
        for i in range(2, n+1):
            term.append(term[i-1] + term[i-2])
        return term[n]