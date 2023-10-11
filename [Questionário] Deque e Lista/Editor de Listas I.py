def editor_de_listas():
    lista = []
    while True:
        comando = input().split()
        if comando[0] == 'I':
            lista.insert(0, int(comando[1]))
        elif comando[0] == 'F':
            lista.append(int(comando[1]))
        elif comando[0] == 'P':
            if lista:
                print(lista.pop())
            else:
                print("Lista vazia")
        elif comando[0] == 'D':
            if lista:
                print(lista.pop(0))
            else:
                print("Lista vazia")
        elif comando[0] == 'X':
            for i in lista:
                print(i)
            break
            

editor_de_listas()