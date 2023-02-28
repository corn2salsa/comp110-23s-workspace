"""One shot wordle!"""
__author__: str = "730614170"

SECRET: str = "python"
SECRET_LENGTH: int = len(SECRET)
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
emoji: str = ""

word: str = input(f'What is your {SECRET_LENGTH}-letter guess? ')

while len(word) != len(SECRET):
    wrong_length: str = input(f'That was not {SECRET_LENGTH} letters! Try again: ')
    word = wrong_length

while idx < len(SECRET):
    if word[idx] == SECRET[idx]:
        emoji = emoji + GREEN_BOX
    else:
        idx_yellow: int = 0
        possible_yellow: bool = False
        while not possible_yellow and idx_yellow < SECRET_LENGTH:
            if SECRET[idx_yellow] == word[idx]:
                possible_yellow = True
            else:
                idx_yellow = idx_yellow + 1
        if possible_yellow:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    idx = idx + 1

print(emoji)

if word == SECRET:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")