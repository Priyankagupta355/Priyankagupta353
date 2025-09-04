# Simple Quiz Application

# Dictionary to store questions and answers
quiz = {
    "1. What is the capital of India?": "Delhi",
    "2. Who developed Python?": "Guido van Rossum",
    "3. Which is the largest planet in our Solar System?": "Jupiter",
    "4. What is the output of 2**3 in Python?": "8",
    "5. Which keyword is used to exit a loop in Python?": "break"
}

print("🎯 Welcome to the Quiz Game!")
print("Type your answer correctly (case sensitive). Let's begin!\n")

score = 0
total_questions = len(quiz)

# Iterating through each question
for question, answer in quiz.items():
    print(question)
    user_answer = input("Your Answer: ")

    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {answer}\n")

# Calculating Percentage
percentage = (score / total_questions) * 100

print("🎉 Quiz Completed!")
print(f"✅ You got {score}/{total_questions} correct.")
print(f"📊 Your Score: {percentage:.2f}%")
