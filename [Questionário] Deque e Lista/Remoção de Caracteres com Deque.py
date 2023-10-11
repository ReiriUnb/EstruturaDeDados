from collections import deque

def process_sequence(input_sequence):
    d = deque()
    removed_chars = []

    for char in input_sequence:
        if char.isalpha() or char.isspace() or char == ',' or char == '.' or char == '>':
            d.appendleft(char)
        elif char.isdigit():
            d.append(char)
        elif char == '*':
            if len(d) > 0:
                removed_chars.append(d.popleft())
        elif char == '+':
            if len(d) > 0:
                removed_chars.append(d.pop())

    return ''.join(removed_chars)


input_sequence = input()
print(process_sequence(input_sequence))