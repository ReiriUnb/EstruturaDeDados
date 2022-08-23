def soma(x):
    if len(x) == 1:
        print(x[0])
        return x[0]
    print(f'{x[0]} + soma({x[1:]})')
    return x[0] + soma(x[1:])
n = int(input())
x = [(2*x) - 1 for x in range(1, n+1)]
q = soma(x)
print('---------------')
print(f'{n} ** 2 == {q}')
