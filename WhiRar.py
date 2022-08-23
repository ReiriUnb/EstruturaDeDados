#numero_bit = 5


def letra(numero):
    Nun_Da_letra = ord('A') + numero - 1 #representar o numero que letra vai ser 'a =1, b=2' (e ord vai me retornar valor interiro que corresponde o numero de caracter q repesenta na memoria do pc)
    return chr(Nun_Da_letra) #chr vai converter o numero para o caracter correspondente da interaçaõ
def decompress(x):
    if x == 0:
        return ''
    bits = x % (2 ** 5)
    x = x // (2 ** 5)
    return f'{letra(bits)}{decompress(x)}'

print(decompress(65))

