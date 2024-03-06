import random

def toss():
    print("Let's toss to decide who will bat first.")
    choice = input("Choose 'odd' or 'even': ").lower()
    if choice not in ['odd', 'even']:
        print("Invalid choice. Please choose 'odd' or 'even'.")
        toss()
    player_1 = int(input("Enter a number between 1 and 6: "))
    AI = random.randint(1, 6)
    total = player_1 + AI
    print(f"You chose {player_1}. Computer chose {AI}.")
    if total % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    if choice == result:
        print("You won the toss! What do you choose?")
        return True
    else:
        print("Computer won the toss! It chooses to bat first.")
        return False

def play_game():
    batting_first = toss()
    if batting_first:
        print("You chose to bat first.")
        player_score = 0
        while True:
            player_input = int(input("Enter a number between 1 and 6: "))
            AI_input = random.randint(1, 6)
            print(f"You chose {player_input}. Computer chose {AI_input}.")
            if player_input == AI_input:
                print("You are out!")
                break
            player_score += player_input
            print("Your total score is:", player_score)
        print("Your final score is:", player_score)
        print("Now, it's computer's turn to bat.")
        AI_score = 0
        while True:
            AI_input = random.randint(1, 6)
            player_input = int(input("Enter a number between 1 and 6: "))
            print(f"Computer chose {AI_input}. You chose {player_input}.")
            if player_input == AI_input:
                print("Computer is out!")
                break
            AI_score += AI_input
            print("Computer's total score is:", AI_score)
        print("Computer's final score is:", AI_score)
    else:
        print("Computer chose to bat first.")
        AI_score = 0
        while True:
            AI_input = random.randint(1, 6)
            player_input = int(input("Enter a number between 1 and 6: "))
            print(f"Computer chose {AI_input}. You chose {player_input}.")
            if player_input == AI_input:
                print("Computer is out!")
                break
            AI_score += AI_input
            print("Computer's total score is:", AI_score)
        print("Computer's final score is:", AI_score)
        print("Now, it's your turn to bat.")
        player_score = 0
        while True:
            player_input = int(input("Enter a number between 1 and 6: "))
            AI_input = random.randint(1, 6)
            print(f"You chose {player_input}. Computer chose {AI_input}.")
            if player_input == AI_input:
                print("You are out!")
                break
            player_score += player_input
            print("Your total score is:", player_score)
        print("Your final score is:", player_score)
    
    if player_score > AI_score:
        print("Congratulations! You won the game.")
    elif player_score < AI_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("It's a tie!")

play_game()
