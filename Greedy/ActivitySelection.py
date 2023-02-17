class Activity:
    def __init__(self, start=None, finish=None):
        self.start = start
        self.finish = finish


class ActivitySelection:
    def solution(self, arr):
        sorted(arr, key=lambda x: x.finish)
        res = list()
        res.append(arr[0])

        for i in range(1, len(arr)):
            if res[-1].finish <= arr[i].start:
                res.append(arr[i])
        for a in res:
            print(a.start, a.finish)


if __name__ == "__main__":
    arr = list()
    arr.append(Activity(1, 3))
    arr.append(Activity(2, 5))
    arr.append(Activity(3, 4))
    arr.append(Activity(4, 7))
    arr.append(Activity(7, 10))
    arr.append(Activity(8, 9))
    arr.append(Activity(9, 11))
    arr.append(Activity(9, 13))
    arr.append(Activity(11, 12))
    arr.append(Activity(12, 14))

    acs = ActivitySelection()
    acs.solution(arr)
    pass
