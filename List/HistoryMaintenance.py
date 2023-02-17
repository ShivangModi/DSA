from Stack import Stack


class HitoryMaintenance:
    def __init__(self):
        self.__history = Stack()

    def loadWebsite(self, url):
        self.__history.push(url)

    def loadRecent(self):
        print(self.__history.peek())

    def deleteRecentNHistory(self, n):
        for i in range(n):
            self.__history.pop()

    def sizeOfHistory(self):
        print(self.__history.len())
