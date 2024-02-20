class Jar:
    def __init__(self, capacity=12):
        try:
            if capacity >= 0:
                self._capacity = capacity
            else:
                raise ValueError("Bad integer")
        except:
            raise ValueError("Bad integer")

        self._size = 0

    def __str__(self):
        contents = ""
        for _ in range(self.size):
             contents += "🍪"
        return contents

    def deposit(self, n):
        current = self.size
        if current + n > self.capacity:
                raise ValueError("Exceeds capacity")
        else:
            self._size +=n

    def withdraw(self, n):
        current = self.size
        if current < n:
                raise ValueError("Don't have that many")
        else:
            self._size -=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size