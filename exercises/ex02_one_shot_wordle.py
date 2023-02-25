"""One shot wordle"""
__author__: "730614170"

secret: str = "python"
playing: bool = True
guesses: int = 1 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word: str = input("What is your " + str(len(secret)) + "-letter guess? ")
idx: int = 0
emoji: str = ""
idx_yellow: int = 0
possible_yellow: bool = False


while len(word) != len(secret):
    word: str = input("That was not " + str(len(secret)) + "-letters! Try agin: ")
    guesses = guesses + 1
    
    if guesses == int(6):
      print("Not quite. Play again soon! ")
      exit()


while len(emoji) < len(secret):
    if word[idx] == secret[idx]:
        emoji = emoji + GREEN_BOX
    else:
        while not possible_yellow and idx_yellow < len(secret):
            if secret[idx_yellow] == word[idx]:
                possible_yellow = True
            idx_yellow = idx_yellow + 1
        if possible_yellow:
            emoji = emoji + YELLOW_BOX
            possible_yellow = False
        else:
            emoji = emoji + WHITE_BOX
    idx = idx + 1

if word == secret:
    print(emoji)
    print("Woo! You got it!") 
else: 
    print(emoji)
    print("Not quite. Play again soon!")
    exit()