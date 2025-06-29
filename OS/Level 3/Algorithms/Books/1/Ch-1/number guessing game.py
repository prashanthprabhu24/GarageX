"""
This python file contains my self written implementation of CLI Number Guessing Game using
Binary Search Algorithm as per books explanation
"""

def number_guess():
    print("🎯 Think of a number between 1 and 100, and I will guess it!")
    print("🤖 Respond with: 'h' for too high, 'l' for too low, 'c' for correct.")
    low = 1
    high = 100
    guesses = 0
    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        print(f"🤔 Is your number {guess}?")
        response = input("👉 Your response (h/l/c): ").lower().strip()
        if response == 'c':
            print(f"🎉 Yay! I guessed your number in {guesses} tries!")
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        else:
            print("⚠️ Invalid input. Please enter 'h', 'l', or 'c'.")
    if low > high:
        print("🤖 Hmm... Seems like there's a mistake or a lie in your responses 😅")


number_guess()
