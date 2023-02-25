"""fuck"""

secret: int = 48
guess: int = int(input("Guess, idiot. "))
playing: bool = True
guesses: int = 0

while playing:
    if guesses == 3:
        print("no more, wench")
        playing = False
    if guess == secret:
        print("yay")
        playing = False
    else:
         print("you are weak like snail")
         guess
         if guess > secret:
            print("too hi")
         if guess % 2 != 0:
            print("that jawn aint odd")
    guesses = guesses + 1

