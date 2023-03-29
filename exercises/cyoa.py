"""Would You Survive a Zombie Apocalypse?"""
__author__: "730614170"

player: str = ""
points: int = 0
ZOMBIE_EMOJI: str = "\U0001F9DF"


def main() -> None:
    """Main."""
    greet()
    global points
    playing: bool = True
    while playing == True:
        print(f"You have accumulated {points} points! Wow that's impressive!")
        print("You have enetred the Apocalypse! Select your first path!")
        print(f'1. Become a zombie for a day{ZOMBIE_EMOJI}! 2. Team up with a group. 3. Go solo(or maybe with a dog friend)!')
        first: int = input("Select from above: ")
        if first == "1":
            print("You see a friendly zombie!")
            print("He says he only wants a nibble off your shoulder.")
            print("You oblidge!")
            print("You have died(obviously, it's the apocalypse).")
            print("Maybe don't do that next time - Bye!")
            print(f"You have accumulated {points} points! Wow that's impressive!")
            playing = False
        if first == "2":
            points_2: int = 0
            points = points + group(points_2)
        if first == "3":
            solo_dolo()
   

def greet() -> None:
    """Greeting the player."""
    global player
    print("Welcome to the Zombie Apocalypse!")
    print("Everything has gone to shit, and it is your job to try to survive in this moraly destitute world.")
    print("Continue through the game, selecting various paths to accumulate points. Do you have what it takes???")
    name: str = input(f"What is your name, survivor? ")
    player = name
    print(f'Hello, {player}')


def group(points: int) -> int:
    """Group path."""
    points
    global player
    import random
    starter: int = random.randint(8,46)
    print(f"You have found a group of {starter} that seem pretty cool")
    print(f'Welcome to "The Squad", {player}')
    print("You are accepted into their small village")
    print("They ask what job you'd like")
    first: int = input("1. Backsmith OR 2. Farmer: ")
    if first == "1":
        points = points + 2
    else: 
        points = points + 1
    print("You enjoy your work for some time but start to notice odd things about the group")
    print("It's getting a little culty in here")
    print("Our leader is the pastor")
    print("OOP - The pastor just slapped a little girl ")
    print("It's definitely time to leave")
    print("Let them know first?(it would be courteous)")
    second: int = input("1. Yes OR 2. Hell No!: ")
    if second == "1":
        points = points + 2
        print("Woah the pastor looks upset")
        print("This was a bad idea")
        print("yep he's gonna use you as an example")
        print("Wow he's about to crucify you")
        print("This has to be sacreligious, right??")
        print("You have died")
        return points
    if second == "2":
        points = points + 6
        print("Smart, you made it out")
        return points


def solo_dolo() -> None:
    """Solo Adventure!"""
    global points
    global player
    points = points + 1
    print(f'Hello, {player}! Welcome to the Apocalypse: Solo Edition.')
    print("Since you're determined to be alone you must choose from the following:")
    first: int = input("1. Kill and eat your mom OR 2. just kill your mom: ")
    if first == "1":
        points = points + 2
        print("Weird choice! But hey, who's judging in the Apocalypse?")
    else:
        points = points + 1
        print("Horrible! See you in hell!")
    print("you see a cute doggy!")
    second: int = input("1. Give it some food(your mom) OR 2. Kill and eat it: ")
    if second == "1":
        points = points + 3
        print("Yes! you now have a dog that can do cool things like backflips and bite zombies!")
    else: 
        points = points + 1
        print("Dude what is wrong with you?")
    print("it's been raining a lot recently")
    print("You're cold and need to seek shelter")
    third: int = input("1. Find an abandonded house OR 2. Hole up in the dilapidated Walmart: ")
    if third == "1":
        points = points + 1
        print("Wow this place is really nice")
        print("It's furnished beautifully and the var-")
        print("You set off a trip wire that causes an explosion to your left")
        print("Your ears are ringing with you lie, bloodied, on the floor")
        print("Someone grabs you but you blackout")
        print("You wake up in a dark cellar with a man and a woman before you")
        print("The man asks if you have any useful skills")
        fourth_1: int = input("1. yes OR 2. no: ")
        if fourth_1 == "2":
            points = points + 1
            print("dude why would you admit that")
            print("the woman shoots you in the head")
            return
        else:
            points = points + 3
            print("You panic and say you know how to ferment vodka")
            print("Really weird pick but they seem interested")
            print("They ask you what you need to get started")
            fifth_1: int = input("1. Boric Acid OR 2. 45 potatos")
            if fifth_1 == "1":
                points = points + 1
                fifth_1 = "Boric Acid"
            else:
                points = points + 2
                fifth_1 = "45 potatoes"
            print("You are so bad under pressure")
            print("They feed you and leave you be for a few days")
            print("You give up trying to ferment and hatch a plan to escape")
            print("One day when they are feeding you, you see an opening for escape")
            print(f'you throw your {fifth_1} at the woman and run out of the cellar')
            sixth_1: int = input("1. Head out the back door OR 2. Head out the front door: ")
            if sixth_1 == "1" or "2":
                points = points + 3
                print("you run outside")
                print("sweet, sweet freedom")
                print("You walk east for a mile before being engulfed by a horde of zombies")
                print("you have died")
                return
    else:
        points = points + 55
        print("Wow it actually isn't dilapidated")
        print("it has everything you need to survive and have fun for the next 55 years")
        print("You don't really have a reason to go anywhere so... I guess you won the apocalypse")
        fourth_2: int = input("1. Stay in the Walmart OR 2. explore the outside world: ")
        if fourth_2 == "1":
            points = points + 100
            print("yeah you won, congrats(em)!")
            return
        if fourth_2 == "2":
            points = points + 5
            print("Points for bravery!")
            print("but death for stupidity :/ ")
            print("You are attacked by a swarm of zombies")
            print("You have died.")
            return
        
if __name__ == "__main__":
    main()