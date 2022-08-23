lista = {0:0}
def fibo(n):
    if n not in lista.keys():
        lista[n] = 1
    else:
        lista[n] += 1
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input())
fib = fibo(n)
print(f"fibonacci({n}) = {fib}.")
z = list(lista.keys())
z.sort()
for x in z:
    print(f"{lista[x]} chamada(s) a fibonacci({x}).")