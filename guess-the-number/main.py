from os import system
import random
def main(number, a, b):

    hiddenNumber = random.randint(a, b)

    if hiddenNumber == number:
        print(f"you guessed it right! its {number}")
    else:
        print(f"you guessed it wrong the number is {hiddenNumber}")
    system("pause")

while True:

    system("cls")

    choice = int(input("1-easy(1-2)\n2-medium(1-5)\n3-hard(1-10)\nchoose your mode: "))

    if choice == 1:
        number = int(input("what's your guess?: "))
        main(number, 1, 2)
    elif choice == 2:
        number = int(input("what's your guess?: "))
        main(number, 1,5)
    elif choice == 3:
        number = int(input("what's your guess?: "))
        main(number, 1, 10)
    else:
        print(KeyError)
        break
