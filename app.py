import random
import re
from os import system

def start():
    system("clear")
    while True:
        text = input("Options:\n\t1. Dice Roller - 'droll'\n")
        parse_input(text)

def parse_input(text):
    print("")
    if text == "q":
        return True
    elif text == "droll" or text == "1":
        dice_roller()
        return False

def dice_roller():
    system("clear")
    while True:
        print("Enter your dice ('q' to go back)\n\n")
        dice = input().split(" ")
        if len(dice) > 0:
            if dice[0] == 'q':
                return
            else:
                for die in dice:
                    pattern = re.compile("\d+d\d+")
                    if pattern.match(die):
                        values = die.split("d")
                        output = ""
                        for i in range(int(values[0])):
                            output = output + str(get_random(values[1])) + ", "
                        print(die+': '+output.strip(", ")+'\n')
                        
def get_random(max):
    return random.randint(1, int(max))

start()