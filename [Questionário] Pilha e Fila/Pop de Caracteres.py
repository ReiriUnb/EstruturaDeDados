def process_sequence(sequence):
    stack = []
    result = ''
    
    for char in sequence:
        if char != '*':
            stack.append(char)
        elif stack:
            result += stack.pop()
    
    return result

sequence = input("Digite a sequência de caracteres: ")
print(process_sequence(sequence))
