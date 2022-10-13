from sense_hat import SenseHat
import random

s = SenseHat()
red = (255, 0, 0)
white = (0, 0, 0)

def rollAdice(n):
    dice = random.randint(1, n)  # where the endpoints are included
    return dice

while True:
    try:
        x = int(input("please enter an integer between 1 and 64: "))
        if 0 < x <= 64:
            ndice = rollAdice(x)
            diceList = []
            for i in range(64):
                if i < ndice:
                    diceList.append(red)
                else:
                    diceList.append(white)
            s.set_pixels(diceList)
        else:
            print("Enter a validate integer between 1 and 64. Try again. ")

    except ValueError:
        print("Warning! Enter an integer within the range. Try again. ")

