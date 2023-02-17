class Task:
    def __init__(self, deadline=None, profit=None):
        self.deadline = deadline
        self.profit = profit


class TaskScheduling:
    def solution(self, arr, t):
        sorted(arr, key=lambda x: x.profit, reverse=True)
        assign = [True] * t
        task = [Task()] * t

        for t in arr:
            i = t.deadline - 1
            while any(assign[:t.deadline]) and i >= 0:
                if assign[i]:
                    task[i] = t
                    assign[i] = False
                    break
                i -= 1
        for t in task:
            print(t.deadline, t.profit)
        pass


if __name__ == "__main__":
    arr = list()
    arr.append(Task(4, 70))
    arr.append(Task(2, 60))
    arr.append(Task(4, 50))
    arr.append(Task(3, 40))
    arr.append(Task(1, 30))
    arr.append(Task(4, 20))
    arr.append(Task(6, 10))

    ts = TaskScheduling()
    ts.solution(arr, 6)
    pass
