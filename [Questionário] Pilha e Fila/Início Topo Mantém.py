class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, data):
        self.items.insert(0, data)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]
