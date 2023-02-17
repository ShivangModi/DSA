class StringMatching:
    @staticmethod
    def KMP(s):
        f = [0] * len(s)
        idx = 0
        for i in range(1, len(s)):
            if s[i] == s[idx]:
                f[i] = f[i - 1] + 1
                idx += 1
            else:
                idx = 0
        print(f)


if __name__ == "__main__":
    # string = "abacab"
    string = "ababaca"
    sm = StringMatching()
    sm.KMP(string)
