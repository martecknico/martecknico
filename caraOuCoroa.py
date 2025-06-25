import random as rd
escolha= input("Cara ou Coroa? ")
lista = ["cara","coroa"]
sorteio = rd.choice(lista)

if escolha.lower() == sorteio:
    print("Você ganhou.", "Deu ",sorteio)
else:
    print("Você perdeu.", "Deu",sorteio)