from collections import deque

def process_sequence(sequence):
    queue = deque()
    result = ''
    
    for char in sequence:
        if char != '*':
            queue.append(char)
        elif queue:
            result += queue.popleft()
    
    return result

sequence = input()
print(process_sequence(sequence))
