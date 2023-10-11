class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)

    def print_table(self):
        for i in range(self.size):
            if self.table[i]:
                print(f'{i} - {" -> ".join(map(str, self.table[i]))}')
            else:
                print(f'{i} - [x]')

T, N = map(int, input().split())
keys = list(map(int, input().split())) if N > 0 else []
hash_table = HashTable(T)
for key in keys:
    hash_table.insert(key)
hash_table.print_table()
