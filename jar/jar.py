class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError('Negative integer')
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError('Deposit exceeds capacity')

    def withdraw(self, n):
        if self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError('Withdrawal exceeds cookie population')

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, cookies):
        self._size = cookies
