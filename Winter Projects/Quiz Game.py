import math 
import random

# Introduction section 
def introduction():
    print("Welcome to Winter Quizorama!")    
    print("Im your host Wintermen, and I welcome you to my show!")
    print("I will now go over the rules of the quiz show!")
    print("The first rule is to not use the Internet AT ALL. The answer must come from the brain of yours.")
    print("Rule number two is that you have 20 seconds to figure out the answer before the opposing opponent gets a chance to answer.")
    print("The rule that most people are wondering is, who goes first. Flip a coin and figure that out.")
    print("Lastly have fun!")
    yes = input("Do you understand (yes/no): ").lower()
    if yes == "no":
        print("Stop playing this game immidiately.")
        quit()
    return None
print(introduction())
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

