import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(min_val, max_val):
    return random.randint(min_val, max_val)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ")
    try:
        return int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return displayProblem(num1, num2, operation)

def isCorrect(user_answer, correct_answer, attempts):
    if user_answer == correct_answer:
        print("Correct!")
        return 10 if attempts == 1 else 5
    else:
        print("Incorrect. Try again." if attempts == 1 else "Incorrect again.")
        return 0

def displayResults(score):
    print(f"\nYour final score: {score}/100")
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    elif score > 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Your rank: {grade}")

def getDifficultyRange(level):
    if level == 1:  
        return 1, 9
    elif level == 2: 
        return 10, 99
    elif level == 3:  
        return 1000, 9999
    else:
        print("Invalid difficulty level. Defaulting to Easy.")
        return 1, 9

def playQuiz():
    displayMenu()
    try:
        level = int(input("Choose a difficulty level (1, 2, 3): "))
    except ValueError:
        print("Invalid input. Defaulting to Easy.")
        level = 1

    min_val, max_val = getDifficultyRange(level)
    score = 0

    for i in range(10):
        num1 = randomInt(min_val, max_val)
        num2 = randomInt(min_val, max_val)
        operation = decideOperation()
        correct_answer = num1 + num2 if operation == '+' else num1 - num2

        print(f"Question {i + 1}: ")
        attempts = 0

        while attempts < 2:
            user_answer = displayProblem(num1, num2, operation)
            points = isCorrect(user_answer, correct_answer, attempts + 1)
            score += points
            if points > 0:
                break
            attempts += 1

    displayResults(score)

def main():
    while True:
        playQuiz()
        again = input("\nWould you like to play again? (yes or no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Well Played! Goodbyee!")
            break

if __name__ == "__main__":
    main()
