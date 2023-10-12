from collections import deque

def process_queue():
    names = input().split()
    X = int(input())

    queue = deque(names)

    # Avançar na fila X vezes
    for _ in range(X):
        queue.rotate(-1)

    print("Pessoa da frente:", queue[0])
    print("Pessoa do fim:", queue[-1])

process_queue()
