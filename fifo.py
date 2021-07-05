class Fifo:
    def __init__(self):
        self.__list = []
    
    def push(self, val):
        self.__list.append(val)
    
    def pop(self):
        val = self.__list[-1]
        del self.__list[-1]
        return val