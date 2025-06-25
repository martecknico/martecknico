from random import randint
print("Welcome")
secret = randint(1,10)
guess = 0
attempt=0
while guess != secret and attempt<3:
    g = input("Guess a number between 1 and 10: ")
    guess = int(g)
    if guess == secret:
        print("You Win!!!")
    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")
    attempt+=1
print("Game Over")