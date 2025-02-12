print("Guessing game")
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, print to the input box (This is specific to this platform)


# Three Loop Questions:
# 1. What do I want to repeat?
#  ->
# 2. What do I want to change each time?
#  ->
# 3. How long should we repeat?
#  ->

# Set a fixed number instead of using random
correct_number = 42
attempts = 7  # Number of allowed guesses

print("Welcome to the Guessing Game!")
print(f"You have {attempts} attempts to guess the correct number between 1 and 100.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

    if guess == correct_number:
        input(
            "🎉 Congratulations! You guessed the correct number! Press Enter to exit."
        )
        break
    elif guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attempt == attempts:
        input(
            f"❌ You've used all your attempts! The correct number was {correct_number}. Press Enter to exit."
        )
