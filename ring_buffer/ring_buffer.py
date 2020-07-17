class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.amount = 0

    def append(self, item):
        self.buffer[self.amount] = item
        self.amount+= 1
        if self.amount == self.capacity:
            self.amount = 0

    def get(self):
        return [item for item in self.buffer if item !=None]


# https://www.youtube.com/watch?v=F2MIRFCjfU0
# vid i used

buffer = RingBuffer(3)



buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')

print(buffer.get())

buffer.append('e')
buffer.append('f')

print(buffer.get())




