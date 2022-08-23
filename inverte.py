def inverte(frase):
    if frase == '':
        return frase
    return frase[-1] + inverte(frase[:-1])

mensagem = input()

print(inverte(mensagem))