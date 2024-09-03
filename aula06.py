lista = [1,45,23,12,11,6,8,4,34,19,14]

lista.sort()
lista.sort(reverse=True)
print(f'Lista ordenada {lista}')

lista.remove(12)
lista.pop(5)
del lista[2:5]

nome = 'Kauan'
lista.append(nome)
print(lista)

lista.insert(2, 'Ribeiro')
print(lista)

# Substituição
lista[2] = 'Vinicius'
print(lista)

print('Kauan' in lista)

if 'Kauan' in lista:
    # esse bloco so sera executado quando a condiçao e true
    print("sim, o kauan esta na lista")
else:
    #esse bloco so sera executado quando a condiçao e false
    print("nao, o kauan nao esta na lista")

notas = []
print(30*'-', 'BOLETIM ESCOLAR' ,30*'-')
numero_usuario1 = int(input('Digite um numero: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite um numero: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite um numero: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite um numero: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite um numero: '))
notas.append(numero_usuario5)

# Len conta a quantidade de elementos dentro da lista
quantidade_notas = len(notas)

# sum ira somar todos os elementos da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f'As notas são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A media é: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperção >= 5 
    Reprovado
'''
if media >= 7:
    print(f'Aprovado com media {media}')

elif media >= 5:
    print(f'Recuperação com media {media}')

else:
    print(f'Reprovado com media {media} ')
