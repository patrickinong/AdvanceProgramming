import random

def load_jokes(file_path):
    """Load jokes from a file, each in the format 'setup?punchline'."""
    with open(file_path, 'r') as file:
        jokes = file.readlines()
    return [joke.strip() for joke in jokes]

def tell_joke(jokes):
    """Tell a random joke from the list."""
    joke = random.choice(jokes)
    
    if '?' in joke:
        setup, punchline = joke.split('?', 1)
    else:
        setup, punchline = joke, "No punchline available."
    
    print(f"Setup: {setup}")
    input("Press Enter to see the punchline...")
    print(f"Punchline: {punchline}")

def main():
    jokes = load_jokes('randomJokes.txt')
    print("Welcome! You can ask me to tell a joke anytime.")
    
    while True:
        user_input = input("Type 'Alexa tell me a Joke' for a new joke or 'quit' to exit: ").lower()
        if user_input == "alexa tell me a joke":
            tell_joke(jokes)
        elif user_input == "quit":
            print("Goodbye!")
            break
        else:
            print("I didn't understand that. Please type 'Alexa tell me a Joke' or 'quit'.")

if __name__ == "__main__":
    main()
