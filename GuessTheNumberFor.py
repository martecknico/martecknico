from random import randint
print("Welcome")
secret = randint(1,10)
guess=0

for i in range(3):
    guess=input("Guess the number ")
    g=int(guess)
    if g>secret:
        print("Too High")
    elif g<secret:
        print("Too Low")
    elif g==secret:
        print("You win!!!")
    else:
        print("You Lose")

print("Game Over")