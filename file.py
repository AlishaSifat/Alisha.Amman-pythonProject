def alisha_calculator():
 print("Simple Calculator")
num1 = int(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))
if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")
else:
    print("Invalid operation")


    def amman_guessing_game():
        import random

    print("Welcome to the Guessing Game!")

    while True:
        secret_number = random.randint(1, 50)
        attempts = 0

        print("\nI have selected a number between 1 and 50.")
        print("Try to guess it!")

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Simple Calculator")
        print("2. Guessing Game")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            alisha_calculator()
        elif choice == "2":
            amman_guessing_game()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
