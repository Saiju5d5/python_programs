questions = [
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Sarojini Naidu", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Which element is necessary for the formation of rust?",
        "options": ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"],
        "answer": "Oxygen"
    },
    {
        "question": "Who is known as the Iron Man of India?",
        "options": ["Jawaharlal Nehru", "Subhash Chandra Bose", "Sardar Patel", "Mahatma Gandhi"],
        "answer": "Sardar Patel"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["1942", "1945", "1947", "1950"],
        "answer": "1947"
    }
]
prizes =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]
lifeline_used = False

print("Welcome to Kaun Banega Crorepati!")
print("Answer the questions correctly to win cash prizes!\n")

for i in range(len(questions)):
    # Display the question and options
    print(f"\nQuestion {i + 1}: {questions[i]['question']}")
    for idx, option in enumerate(questions[i]['options'], 1):
        print(f"{idx}. {option}")
    
    # Offer 50:50 lifeline if not used yet
    if not lifeline_used:
        use_lifeline = input("\nDo you want to use the 50:50 lifeline? (y/n): ").strip().lower()
        if use_lifeline == "y":
            lifeline_used = True
            print("\n50:50 Lifeline Activated!")
            correct_answer = questions[i]['answer']
            incorrect_options = [opt for opt in questions[i]['options'] if opt != correct_answer]
            removed_options = random.sample(incorrect_options, 2)
            print(f"Remaining Options: ")
            for idx, option in enumerate(questions[i]['options'], 1):
                if option not in removed_options:
                    print(f"{idx}. {option}")
    
    # Get the user's answer
    while True:
        try:
            choice = int(input("\nEnter the number of your answer (1-4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a valid number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Check if the answer is correct
    user_answer = questions[i]['options'][choice - 1]
    if user_answer == questions[i]['answer']:
        print(f"Correct! You've won ₹{prizes[i]}")
    else:
        print(f"Wrong answer! The correct answer was {questions[i]['answer']}. You won ₹{prizes[i-1] if i > 0 else 0}.")
        break
else:
    print("Congratulations! You've won the top prize of ₹1,00,000!")