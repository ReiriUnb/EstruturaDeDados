class Stack:
    def __init__(self):
       self.items = []

    def isEmpty(self):
       return self.items == []

    def push(self, item):
       self.items.append(item)

    def pop(self):
       return self.items.pop()

    def peek(self):
       return self.items[-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class PriorityQueue:
    def __init__(self):
       self.items = []

    def isEmpty(self):
       return self.items == []

    def enqueue(self, item):
       self.items.append(item)

    def dequeue(self):
       self.items.sort()
       return self.items.pop()

    def front(self):
       return self.items[len(self.items) - 1]


for i in range(5):
   n = int(input())
   lifo = Stack()
   fifo = Queue()
   pfifo = PriorityQueue()
   
   p = f = pf = 1  
   for _ in range(n):
     op, elm = input().split()
     elm = int(elm)
     
     if op == 'in':
        lifo.push(elm)
        fifo.enqueue(elm)
        pfifo.enqueue(elm)
     elif op == 'out':
        if elm != lifo.peek():
            p = 0
        elif p == 1:
            lifo.pop()
        if elm != fifo.front():
            f = 0
        elif f == 1:
            fifo.dequeue()
        if pf == 1:
            x = pfifo.dequeue()
            if x != elm:
                pf = 0

   if p + f + pf > 1:
        print("uai?")
   elif p + f + pf == 0:
        print("no hay!")
   elif p == 1:
        print("LIFO")
   elif f == 1:
        print("FIFO")
   elif pf == 1:
        print("AIPO")
