"""MY FIRST PROGRAM FOR COMP110."""
__author__ = "730614170"

SECRET: str = "python"
playing: bool = True
guesses: int = 1 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word: str = input("What is your " + str(len(SECRET)) + "-letter guess? ")
x: int = 0
emoji: str = ""
idx_yellow: int = 0
possible_yellow: bool = False


while len(word) != len(SECRET):
    word: str = input("That was not " + str(len(SECRET)) + "-letters! Try agin: ")
    guesses = guesses + 1
    
    if guesses == int(6):
      print("Not quite. Play again soon! ")
      exit()


while x < len(word):
    if SECRET(x) == word(x):
        emoji = emoji + GREEN_BOX
    else:
        while not possible_yellow and idx_yellow < len(SECRET):
            if SECRET(idx_yellow) == word(x):
                possible_yellow = True
            else: 
                idx_yellow = idx_yellow + 1
        if possible_yellow:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    x = x + 1

if word == SECRET:
    print(emoji)
    print("Woo! You got it!") 
else: 
    print(emoji)
    print("Not quite. Play again soon!")
    exit()


