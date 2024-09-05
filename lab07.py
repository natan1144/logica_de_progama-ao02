impar = []
soma = 0

for i in range(1,101):
    if i % 2 != 0:
        impar.append(i)
        soma += i
print(f'Números impares {impar}')
print(f'Quantidade de números exibidos {len(impar)}')
print(f'soma dos números impars {soma}')
