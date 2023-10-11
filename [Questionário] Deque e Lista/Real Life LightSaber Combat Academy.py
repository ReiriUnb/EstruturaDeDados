def exibe_candidatos(deque, pos, ordem):
    if pos < 0 or pos >= deque.size():
        return

    temp_deque = Deque()  
    for _ in range(pos):
        temp_deque.add_rear(deque.remove_front())

    if ordem == 'direta':
        while not deque.is_empty():
            print(deque.remove_front())
    elif ordem == 'inversa':
        while not deque.is_empty():
            temp_deque.add_rear(deque.remove_front())
        while not temp_deque.is_empty():
            print(temp_deque.remove_rear())

    while not temp_deque.is_empty():
        deque.add_front(temp_deque.remove_rear())
    