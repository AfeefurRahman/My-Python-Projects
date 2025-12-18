import math 
import random
import time 

# --- 1. Introduction ---
def introduction():
    print("Welcome to Winter Quizorama!")    
    print("I'm your host Robert Frost, and I welcome you to my show!")
    print("I will now go over the rules of the quiz show!")
    print("1. No Internet.")
    print("2. You have 60 seconds to answer.")
    print("3. We flip a coin to see who starts.")
    print("Lastly have fun!")
    yes = input("Do you understand (yes/no): ").lower()
    if yes == "no":
        print("Stop playing this game immediately.")
        quit()
    return None

# --- 2. Coin Flipper ---
def coinFlip():
    choice1 = input("\nPlayer 1, choose between heads or tails: ").lower().strip()

    if choice1 != "heads" and choice1 != "tails":
        print("Invalid choice. We will assume you meant HEADS.")
        choice1 = "heads"

    outcome = ["heads", "tails"]
    result = random.choice(outcome)
    
    print("-" * 20)
    print(f"The coin landed on: {result}")

    if result == choice1:
        print("Match! Player 1 goes first.")
        return "Player 1"
    else:
        print("No match. Player 2 goes first.")
        return "Player 2"

# --- 3. Main Quiz ---
def winter_quiz(): 
    introduction()
    currentPlayer = coinFlip()
    p1_Score = 0
    p2_Score = 0
    
    winter_questions = {
        "How many sides does a snowflake have?": "6",
        "What is the freezing point of water in Fahrenheit?": "32",
        "What do animals do to save energy during winter?": "hibernation",
        "What is the shortest day of the year called?": "winter solstice",
        "What color is a polar bear's skin under its fur?": "black",
        "Which pole has penguins: North or South?": "south",
        "What is a heavy snowstorm with strong winds called?": "blizzard",
        "What vegetable is traditionally used for a snowman's nose?": "carrot",
        "What flavor is a traditional candy cane?": "peppermint",
        "What month is Valentine's Day in?": "february",
        "What are the socks hung by the chimney called?": "stockings",
        "What holiday drink is made from eggs, sugar, and milk?": "eggnog",
        "What plant are people supposed to kiss under?": "mistletoe",
        "What is the Jewish Festival of Lights called?": "hanukkah",
        "What is the name of the reindeer in Frozen?": "sven",
        "Who stole Christmas in the famous Dr. Seuss book?": "the grinch",
        "What brings Frosty the Snowman to life?": "magic hat",
        "What is the name of the main elf in the movie Elf?": "buddy",
        "What sport involves sliding stones on ice and sweeping?": "curling",
        "What is the black rubber disc used in hockey called?": "puck"
    }

    question_deck = list(winter_questions.items())
    random.shuffle(question_deck)

    print("\n" + "="*30)
    print("Let the GAMES BEGIN!!!!")
    print("="*30)

    while len(question_deck) > 0:
        question, answer = question_deck.pop()
        print(f"\nQuestions remaining: {len(question_deck)}")
        print(f"{currentPlayer}'s TURN")
        print(f"Question: {question}")
        print("You have 60 seconds... GO!")

        # --- TIMER START ---
        start_time = time.time()
        
        # User can type immediately now!
        user_ans = input(f"{currentPlayer}, answer: ").lower().strip()
        
        # --- TIMER END ---
        end_time = time.time()
        time_taken = end_time - start_time

        # Logic: Check if Answer is Correct AND Time is within limit
        if time_taken > 60:
            print(f"❌ TOO SLOW! You took {int(time_taken)} seconds.")
            # Treat as wrong answer, move to steal logic
            user_ans = "TOO_SLOW" 
        
        if user_ans == answer:
            print(f"✅ Correct! (Time: {round(time_taken, 1)}s)")
            if currentPlayer == "Player 1":
                p1_Score += 1
            else:
                p2_Score += 1
        else:
            if user_ans != "TOO_SLOW":
                print("❌ Wrong Answer!")
            
            # --- STEAL LOGIC ---
            if currentPlayer == "Player 1":
                other_player = "Player 2"
            else:
                other_player = "Player 1"

            print(f"👀 {other_player}, chance to STEAL!")
            
            # Reset timer for the steal
            start_steal = time.time()
            steal_ans = input(f"{other_player}, answer: ").lower().strip()
            end_steal = time.time()
            
            if (end_steal - start_steal) > 60:
                 print("❌ Too slow on the steal!")
            elif steal_ans == answer:
                print(f"✅ STEAL SUCCESSFUL! Point for {other_player}")
                if other_player == "Player 1":
                    p1_Score += 1
                else:
                    p2_Score += 1   
            else:
                print(f"❌ Both wrong! The answer was: {answer}")
        
        # Shows Current Score
        print(f"Score: P1: [{p1_Score}] | P2: [{p2_Score}]")

        # Switches turns
        if currentPlayer == "Player 1":
            currentPlayer = "Player 2"
        else:
            currentPlayer = "Player 1"

    # End of Game
    print("\n" + "="*30)
    print("Game Over")
    print(f"Final Score: Player 1: {p1_Score} | Player 2: {p2_Score}")

    if p1_Score > p2_Score:
        print("🏆 Player 1 Wins!")
    elif p2_Score > p1_Score:
        print("🏆 Player 2 Wins!")
    else:
        print("🤝 It's a Tie!")

winter_quiz()
