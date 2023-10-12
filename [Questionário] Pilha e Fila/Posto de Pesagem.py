class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

n, f, p = map(int, input().split())

Qtrucks = Queue()
for truck in input().split():
    Qtrucks.enqueue(int(truck))

time = i = 0
while not Qtrucks.isEmpty():
    # pega o primeiro da fila
    fst = Qtrucks.dequeue()
    
    if i % f == 0:
        if fst > p:
            time += 10
            Qtrucks.enqueue(fst - 2)
        else:
            time += 5
    else:
        time += 1
    i += 1
print(time)
