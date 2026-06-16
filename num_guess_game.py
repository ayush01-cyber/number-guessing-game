import random
secret_number = random.randint(1,100)

attempt = 0

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it.\n")

while True:
    try:
        guess = int(input("Enter your guess number: "))
        attempt += 1

        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("\n🎉 Congratulations!")
            print("You guessed the number correctly.")
            print(f"Attempts taken: {attempt}")
            break
    except ValueError:
        print("Please enter a valid number.")