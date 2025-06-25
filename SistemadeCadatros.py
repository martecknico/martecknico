welcome = "Welcome to FIA Business School Lyceum."
electives=["Digital Marketing","Stratigic Marketing","Relationship Marketing","SEO","Luxury Marketing"]

name = input("What's your full name? ")


email = input("What's your email? ")
period = input("What's your period? ")

print(electives)
n=0
while True and n<=20:
    
    subject= input("You may choose from the list above: ")

    if subject in electives and n<=20:
        print("It is a valid course. There are", 20-n, "enrollment slots left.")
    elif subject == "exit" or subject == "Exit":
        break
    elif n>20:
        print("You have reached the maximum number of attempts")
        break
    else:
        print("Invalid option. Choose frMom the list below: ", electives)

print("Enrollment Sucessfully Done")