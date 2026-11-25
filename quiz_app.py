print("=" * 40)
print("       WELCOME TO PYTHON QUIZ")
print("=" * 40)

name = input("Enter your name: ")

questions = [
    {
        "question": "1. Who developed Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum",
                    "C. Dennis Ritchie", "D. Elon Musk"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword defines a function?",
        "options": ["A. function", "B. define",
                    "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "3. Which data type stores True or False?",
        "options": ["A. Integer", "B. String",
                    "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "4. Which symbol is used for comments?",
        "options": ["A. //", "B. #",
                    "C. /*", "D. &"],
        "answer": "B"
    },
    {
        "question": "5. Which function displays output?",
        "options": ["A. input()", "B. print()",
                    "C. display()", "D. output()"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid choice! Try again.")
        answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer!")
        print("Correct answer:", q["answer"])

total = len(questions)
percentage = (score / total) * 100

print("\n" + "=" * 40)
print("             QUIZ RESULT")
print("=" * 40)

print("Student Name:", name)
print("Total Questions:", total)
print("Correct Answers:", score)
print("Wrong Answers:", total - score)
print("Final Score:", score, "/", total)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good!")
elif percentage >= 40:
    print("Performance: Average!")
else:
    print("Performance: Needs Improvement!")

print("=" * 40)
print("       THANK YOU FOR PLAYING!")
print("=" * 40)