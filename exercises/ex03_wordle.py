"""Structured Wordle"""
__author__ = "730614170"

def contains_char(guess: str, letter: str) -> bool:
    """Checking for right letters, wrong place"""
    assert len(letter) == 1
    i: int = 0
    possible_yellow: bool = False
    while not possible_yellow and i < len(guess):
        if letter == guess[i]:
            possible_yellow = True
        else:
            i += 1
    if possible_yellow == True:
        return True
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    """letters to emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emoji: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji = emoji + GREEN_BOX
        else:
            character: bool = contains_char(secret, guess[idx])
            if character == True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        idx += 1
    return emoji

def input_guess(integer: int) -> str:
    """correct guess length"""
    word: str = input(f'Enter a {integer} character word: ')
    while len(word) != integer:
        wrong_length: str = input(f"That wasn't {integer} chars! Try again: ")
        word = wrong_length
    return word

def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    guesses: int = 1
    winner: bool = False
    while guesses < 7 and winner == False:
        print(f'=== Turn {guesses}/6 ===')
        guess: str = (input_guess(5))
        print(emojified(guess, secret))
        if guess == secret:
            print(f'You won in {guesses}/6 turns!')
            winner = True
            return
        else:
            guesses += 1
        if guesses == 7:
            print(f'X/6 - Sorry, try again tomorrow!')
            return
        
if __name__ == "__main__":
    main()