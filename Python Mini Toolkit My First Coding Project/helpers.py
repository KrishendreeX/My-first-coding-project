import time
import random


# Game 1
# GRADE CALCULATOR

def get_valid_score(subject_number: int) -> float:
    # Function to get a valid score for a subject, ensuring it's a number between 0 and 100
    while True:
        try:
            user_input = input(f"Enter marks for Subject {subject_number} (0-100): ").strip()
            
            if not user_input:
                print(" Input cannot be empty. Please enter a number.")
                continue
                
            score = float(user_input)
            
            # Catch individual score boundary errors before returning
            if score < 0 or score > 100:
                print(" Invalid input. Marks must be between 0 and 100.")
                continue
                
            return score
        except ValueError:
            print(" Invalid input. Please enter a valid number (e.g., 85 or 92.5).")

# Function to determine letter grade based on average score
def calculate_letter_grade(average: float) -> str:
    """Determines the letter grade based on the calculated average score."""
    if average >= 90:   
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def grade_calculator():
    print("=" * 40)
    print("      Grade Calculator - Final Report      ")
    print("=" * 40)
    
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print(" Invalid input. Number of subjects must be a number greater than zero.")
            return
    except ValueError:
        print(" Invalid input. Please enter a valid whole number of subjects.")
        return

    # Collect scores for each subject and calculate total score
    total_score = 0.0
    for i in range(1, num_subjects + 1):
        score = get_valid_score(i)
        total_score += score

    # Calculate average score and determine letter grade
    average_score = total_score / num_subjects
    letter_grade = calculate_letter_grade(average_score)

    # Beautiful Final Report Display    
    print("\n" + "-" * 30)
    print(f"{'FINAL REPORT':^30}")
    print("-" * 30)
    print(f"Total Subjects  : {num_subjects}")
    print(f"Average Score   : {average_score:.2f}%")
    print(f"Letter Grade    : {letter_grade}")
    print("=" * 40)

# Run the main function when the script is executed
if __name__ == "__main__":
    grade_calculator()
# End of program


# Game 2
# EVEN OR ODD CHECKER

def even_or_odd():
    while True:
        try:
            user_input = input("Enter a number: ").strip()
            if not user_input:
                print("❌ Input cannot be empty. Please enter an integer.")
                continue
            num = int(user_input)
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")
            
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
# End of programme


# Game 3
# Budget Tracker

def budget_tracker():
    transactions = []
    print("Welcome to your Personal Budget Tracker!")
    
    while True:
        # 1. Calculate the current summary figures
        total_income = 0
        total_expenses = 0
        
        for item in transactions:
            if item["type"] == "Income":
                total_income += item["amount"]
            else:
                total_expenses += item["amount"]
                
        net_balance = total_income - total_expenses

        # 2. Display the Dashboard Menu
        print("\n==============================")
        print(f"Current Balance: R{net_balance:.2f}")
        print(f"Total Income:    R{total_income:.2f}")
        print(f"Total Expenses:  R{total_expenses:.2f}")
        print("==============================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View History")
        print("4. Exit")
        print("==============================")

        choice = input("What would you like to do? (1-4): ").strip()

        # 3. Handle Menu Choices
        if choice == "1" or choice == "2":
            # Determine the type based on the user's menu choice
            if choice == "1":
                transaction_type = "Income"
            else:
                transaction_type = "Expense"
                
            category = input(f"Enter the category for this {transaction_type} (e.g., Salary, Food): ").strip()
            
            # Simple numeric input check
            amount_input = input(f"Enter the amount for {category}: R").strip()
            
            try:
                amount = float(amount_input)
                
                # Save the entry as a dictionary and append it to our list
                new_entry = {
                    "type": transaction_type,
                    "category": category,
                    "amount": amount
                }
                transactions.append(new_entry)
                print(f"✔️ Successfully added R{amount:.2f} to {category}!")
                
            except ValueError:
                print("❌ Error: Please enter a valid number for the amount (skip the 'R' symbol).")

        elif choice == "3":
            print("\n--- TRANSACTION HISTORY ---")
            if not transactions:
                print("No transactions logged yet.")
            else:
                # Loop through the list and print each dictionary neatly
                for index, item in enumerate(transactions, start=1):
                    print(f"{index}. {item['type']}: {item['category']} - R{item['amount']:.2f}")

        elif choice == "4":
            print("\nThank you for tracking your budget. Goodbye!")
            break
            
        else:
            print("❌ Invalid option. Please type 1, 2, 3, or 4.")
# End of programme


# Game 4
# Simple Quiz Game

def quiz_game():
    score = 0

    # Question 1
    answer = input("1. What is the capital of South Africa? ").strip().lower()

    if answer in ["pretoria", "bloemfontein", "cape town"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Question 2
    answer = input("2. What is the tallest mountain in the world? ").strip().lower()

    if answer in ["mount everest", "everest"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Question 3
    answer = input("3. What symbol is used for comments in Python? ").strip()

    if answer == "#":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Question 4 
    answer = input("4. How many days does it take for the Earth to orbit the Sun? ").strip().lower()

    if answer in ["365", "365 days", "365.25", "365.25 days"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Question 5 
    answer = input("5. Which instrument has six strings and is very popular in rock music? ").strip().lower()

    if answer in ["guitar", "a guitar"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Final Score
    print("\nQuiz Finished!")
    print("Your score is:", score, "/ 5")
# End of programme 


# Game 5
# Number Guessing Game

def number_guessing_game():
    # Random number between 1 and 50
    secret_number = random.randint(1, 50)

    # Number of attempts
    attempts = 5

    # Welcome and countdown 
    print("🎮 Welcome to the Number Guessing Game!")
    time.sleep(1)

    print("\nGET READY!!!")
    time.sleep(1)

    # Countdown
    print("3")
    time.sleep(1)

    print("2")
    time.sleep(1)

    print("1")
    time.sleep(1)

    print("\nGuess the number between 1 and 50")
    print("You have 5 attempts\n")

    # Game loop
    while attempts > 0:
        try:
            user_input = input("Enter your guess: ").strip()
            if not user_input:
                print("❌ Input cannot be empty. Please enter a number.")
                continue
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number.")
            continue

        if guess == secret_number:
            print("Correct! You win!")
            break

        elif guess < secret_number:
            print("Too low!")
            print("Almost got it")

        else:
            print("Too high!")
            print("So close!!")

        attempts -= 1
        print("Attempts left:", attempts)
        print()

    # If player loses
    if attempts == 0:
        print(" Game Over!")
        print("The number was:", secret_number)
# End of programme
