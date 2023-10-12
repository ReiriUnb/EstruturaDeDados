class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None  # Retorna None quando a pilha está vazia

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None  # Retorna None quando a pilha está vazia

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
