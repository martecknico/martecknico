import random
nome1 = input("Digite o nome do primeiro nome: ")
nome2 = input("Digite o nome do segundo nome: ")
nome3 = input("Digite o nome do terceiro nome: ")
nome4 = input("Digite o nome do quarto nome: ")
nome5 = input("Digite o nome do quinto nome: ")
lista = [nome1, nome2, nome3, nome4, nome5]
escolhido = random.choice(lista)
print("O nome escolhido foi: ", escolhido)