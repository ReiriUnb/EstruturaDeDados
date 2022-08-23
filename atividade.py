lista1 = []
lista2 = []
while True:
    a = input()
    if a == 'fim':
        break
    elif '-' in a:
        opção, tirar = a.split()
        index = lista1.index(tirar)
        lista1.remove(tirar)
        lista2.index()
        lista2.remove(lista2)
    else:
        produto, preço = a.split()
        lista1.insert(0, produto)
        lista2.insert(0, float(preço))
for i in range(len(lista1)):
    print(f'{lista1[i]}: R$ {lista2[i]:.2f}')
print('----------------------')
print(f'{len(lista1)} item(ns): R$ {sum(lista2):.2f}')
