import math 
import random
import time 

# Introduction section 
def introduction():
    print("Welcome to Winter Quizorama!")    
    print("Im your host Wintermen, and I welcome you to my show!")
    print("I will now go over the rules of the quiz show!")
    print("The first rule is to not use the Internet AT ALL. The answer must come from the brain of yours.")
    print("Rule number two is that you have 60 seconds to figure out the answer before the opposing opponent gets a chance to answer.")
    print("The rule that most people are wondering is, who goes first. Flip a coin and figure that out.")
    print("Lastly have fun!")
    yes = input("Do you understand (yes/no): ").lower()
    if yes == "no":
        print("Stop playing this game immidiately.")
        quit()
    return None
print(introduction())

print()
print()

# coin flipper 
def coinFlip():
    # 1. Get the user's choice
    # .strip() removes accidental spaces, .lower() fixes capitalization
    choice1 = input("Choose between heads or tails: ").lower().strip()

    # 2. Check if the user typed something valid
    if choice1 != "heads" and choice1 != "tails":
        print("Invalid choice. Please run the program again and check your spelling.")
        return 

    # 3. Clarify who is who
    if choice1 == "heads":
        print("Player 1 is Heads. Player 2 is Tails.")
    else:
        print("Player 1 is Tails. Player 2 is Heads.")

    # 4. Flip the coin
    outcome = ["heads", "tails"]
    result = random.choice(outcome)
    
    print("-" * 20) # Prints a divider line
    print(f"The coin landed on: {result}")

    # 5. Determine the winner
    if result == choice1:
        print("Match! Player 1 goes first.")
    else:
        print("No match. Player 2 goes first.")
coinFlip()


# Point Tracker System 
def pointSystem():
    point1 = 0
    point2 = 0

    print("Type '1' to give player 1 a point")
    print("Type '2' to give player 2 a point")
    print("Type 'q' to quit")

    while True: 
        print(f"Current Score: P1: {point1} | P2: {point2}")

        choice = input("Who Scored? > ")

        if choice == '1':
            point1 += 1
            print("Point for Player 1!")
        elif choice == '2':
            point2 += 1
            print("Point for player 2!")
        elif choice == 'q':
            print("Final Score:")
            print(f"Player 1: {point1}")
            print(f"Player 2: {point2}")

            if point1 > point2:
                print("Player 1 wins the Winter Quizorama!")
            elif point1 < point2:
                print("Player 2 wins the Winter Quizorama!")
            else:
                print("It's a tie!")
            break
        else:
            print("Invalid input. Type 1, 2, or q.")

# timer system 
t = 20
def countdown(t):
    while t: 
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1
        print("Times up! Reveal your answer!")

 # All the questions section.

def winter_quiz(): 
     
    winter_questions = {
    # Nature & Science
    "How many sides does a snowflake have?": "6",
    "What is the freezing point of water in Fahrenheit?": "32",
    "What do animals do to save energy during winter?": "hibernation",
    "What is the shortest day of the year called?": "winter solstice",
    "What color is a polar bear's skin under its fur?": "black",
    "Which pole has penguins: North or South?": "south",
    "What is a heavy snowstorm with strong winds called?": "blizzard",

    # Traditions & Holidays
    "What vegetable is traditionally used for a snowman's nose?": "carrot",
    "What flavor is a traditional candy cane?": "peppermint",
    "What month is Valentine's Day in?": "february",
    "What are the socks hung by the chimney called?": "stockings",
    "What holiday drink is made from eggs, sugar, and milk?": "eggnog",
    "What plant are people supposed to kiss under?": "mistletoe",
    "What is the Jewish Festival of Lights called?": "hanukkah",

    # Movies & Pop Culture
    "What is the name of the reindeer in Frozen?": "sven",
    "Who stole Christmas in the famous Dr. Seuss book?": "the grinch",
    "What brings Frosty the Snowman to life?": "magic hat",
    "What is the name of the main elf in the movie Elf?": "buddy",

    # Sports
    "What sport involves sliding stones on ice and sweeping?": "curling",
    "What is the black rubber disc used in hockey called?": "puck"
    }














