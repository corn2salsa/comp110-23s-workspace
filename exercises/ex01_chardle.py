"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730614170"

word: str = input("Enter a 5-character word: ")
if len(word) != int(5):
    print("Error: Word must contain 5 charcters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) != int(1):
    print("Error: Character must be a single character.")
    exit()

instance: int = 0 

print("Searching for " + letter + " in " + word)
if letter == word[0]:
    print(letter + " found at index 1")

if letter == word[1]:
    print(letter + " found at index 2")

if letter == word[2]:
    print(letter + " found at index 3")

if letter == word[3]:
    print(letter + " found at index 4")

if letter == word[4]:
    print(letter + " found at index 5")

if word[0] == letter:
    instance = instance + 1

if word[1] == letter:
    instance = instance + 1

if word[2] == letter:
    instance = instance + 1

if word[3] == letter:
    instance = instance + 1

if word[4] == letter:
    instance = instance + 1

if instance == 0:
    print("No instances of " + letter + " found in " + word)

if instance == 1:
    print("1 instance of " + letter + " found in " + word)

if instance == 2:
    print("2 instances of " + letter + " found in " + word)

if instance == 3:
    print("3 instances of " + letter + " found in " + word)

if instance == 4:
    print("4 instances of " + letter + " found in " + word)

if instance == 5:
    print("5 instances of " + letter + " found in " + word)

