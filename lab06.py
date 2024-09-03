lista = []

nome1 = input("Digite um nome: ")
lista.append(nome1)

nome2 = input("Digite um nome: ")
lista.append(nome2)

lista.sort()

if nome1 and nome2 in lista:
    print(f"Sim, o {nome1} e o {nome2} esta adicionado na lista")
else:
    print(f"Nao, o {nome1} e o {nome2} nao esta na lista")

num1 = 10
num2 = 20

if num1 > num2:
    print("e maior")
else:
    print("e menor")
    if num1 < num2:
        print("e menor")
    else:
        print("e maior")
print("fim do bloco if else")



