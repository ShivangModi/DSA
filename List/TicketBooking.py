from Queue import Queue


class TicketBooking:
    def __init__(self):
        self.__rSeat = Queue()
        self.__wSeat = Queue()

    def addToWaitingList(self, arr):
        self.__wSeat.enqueue(arr)

    def reserveSeat(self, name, address):
        arr = {
            'name': name,
            'address': address
        }
        if self.__rSeat.isFull():  # Stack is full
            self.addToWaitingList(arr)
            return
        self.__rSeat.enqueue(arr)

    def cancelTicket(self, ticketId):
        self.__rSeat[ticketId] = self.__wSeat.dequeue()
