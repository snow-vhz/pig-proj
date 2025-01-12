from random import randint
from time import sleep

def roll():
    value = randint(1, 6)
    return value

print("Do you know how to play?? (Y or N)")
know = input("> ")
if know == "N" or know == "n":
    print("Ok so you have to roll (the dice) and whatever number shows, is added to your score. But if the number is 1, your score resets.")
    print("You can pass and let the other player roll if you are afraid of getting a one or whatever your strategy is.")
    print("You can choose which number you have to reach at the start of the game, if your numbers add up to equal or more than the selected number, you win.")
    print("You have to play with someone else or yourself because I CAN'T code AI to play with you, sorry ;(")
    sleep(4)
    print("Okay, I hope you understood, so lets start the game.")
    play = True
else:
    print("I hope you said yes and didn't type nonsense, let's go!!")
    play = True

while play:
    print("place holder for tha game.. haha you lost l m a ooo")
    
    print("Type the number you want to reach! (has to be at least 10)")
    bet = input("> ")
    
    break

# debug:
print(roll())