import numpy
import random
def bars():
    print("-0=======Nermble=======0-")
def final_a():
    global final
    final = random.randint(1000, 9999)
def main():
    final_a()
    x = 0
    while True:
        bars()
        xm = int(input("-Enter guess here-: "))
        if xm > final:
            print("The number is too high")
            x = x + 1
            continue
        elif xm < final:
            print("The number is too low")
            x = x + 1
            continue
        else:
            print("You win!")
            xx = str(x)
            print("It only took you " + xx + " rounds!")
            print("Time for a new round goodluck!")
            break
    main()
def start():
    bars()
    print("The goal of the game is to guess the 4 digit number")
    print("Each round youll see if your number is higher or smaller than the random generated number")
    x = input(("Press enter to start:"))
    main()
start()
