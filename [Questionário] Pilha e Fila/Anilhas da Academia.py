pesos = []
pesototal = 0
count = 0

# Ler os pesos até que 0 seja encontrado (todas as anilhas já informadas)
while True:
    peso = int(input())
    if peso == 0:
        break
    pesos.append(peso)

peso_alvo = int(input())

# Processar a retirada de pesos em ordem inversa
for peso in reversed(pesos):
    pesototal += peso
    count += 1
    print("Peso retirado:", peso)
    if peso == peso_alvo:
        break

# Printar os resultados:
print("Anilhas retiradas:", count)
print("Peso total movimentado:", pesototal)
