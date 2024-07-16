# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "Which island is in the Caribbean?",
        "options": ["A) Maui", "B) St Kitts", "C) St Tropez", "D) Ibiza"],
        "answer": "B"
    },
    {
        "question": "What is 10 + 2?",
        "options": ["A) 5", "B) 12", "C) 88", "D) 26"],
        "answer": "B"
    },
    {
        "question": "What is 100 + 53?",
        "options": ["A) 113", "B) 153"],
        "answer": "B"
    },
        "question": "Is the captital of the Netherlands, Amsterdam?",
        "options": ["A) True", "B) False"],
        "answer": "B"
    },
    # Learners can add more questions here following the same structure
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
