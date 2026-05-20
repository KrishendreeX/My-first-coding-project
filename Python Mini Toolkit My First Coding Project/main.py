import helpers


while True:

    print("\n===== PYTHON MINI TOOLKIT =====")

    print("1. Grade Calculator")
    print("2. Even or Odd Checker")
    print("3. Quiz Game")
    print("4. Number Guessing Game")
    print("5. Budget Tracker")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        helpers.grade_calculator()

    elif choice == "2":
        helpers.even_or_odd()

    elif choice == "3":
        helpers.quiz_game()

    elif choice == "4":
        helpers.number_guessing_game()

    elif choice == "5":
        helpers.budget_tracker()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")