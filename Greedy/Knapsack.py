class Item:
    def __init__(self, weight=None, value=None):
        self.weight = weight
        self.value = value
        # self.pw = pw


class KnapsackProblem:
    def fractionalKnapsack(self, arr, capacity):
        arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

        i = 1
        profit = 0.0
        for item in arr:
            if item.weight <= capacity:
                print(f"Item {i} weight {item.weight} and profit {item.value}")
                capacity -= item.weight
                profit += item.value
            else:
                print(f"Item {i} weight {capacity} and profit {(capacity / item.weight) * item.value}")
                profit += (capacity / item.weight) * item.value
                capacity = 0
                break
            i += 1

        print(f"Total Profit: {profit}")


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

    capacity = 45
    ks = KnapsackProblem()
    ks.fractionalKnapsack(arr, capacity)
