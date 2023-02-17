class CoinChange:
    def coinChange(self, coin, money):
        coin.sort()
        total = 0
        while money > 0 and coin != []:
            print(f"Number of Coin {coin[-1]}: {money//coin[-1]}")
            total += money//coin[-1]
            money = money%coin[-1]
            coin.pop()
        if money != 0:
            print("Error, you can't get coin change")
        else:
            print(f"Total coin: {total}")

if __name__ == "__main__":
    coin = [1, 3, 5, 8]
    money = 61
    obj = CoinChange()
    obj.coinChange(coin, money)
