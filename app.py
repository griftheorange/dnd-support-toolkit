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
                        sum = 0
                        for i in range(int(values[0])):
                            roll = get_random(values[1])
                            sum += roll
                            output = output + str(roll) + ", "
                        output = die+': '+output.strip(", ")+'\nSUM: '+str(sum)+'\nAVG: '+str(sum/float(values[0]))+"\n"
                        print(output)
                        
def get_random(max):
    return random.randint(1, int(max))

start()