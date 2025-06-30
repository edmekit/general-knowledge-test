import random
questions = []

print("Welcome to the Quiz Game!")
print()

print("A. General Knowledge, B.Science, and C. Pop Culture. Choose a Category. Press X to exit.")
choice = input("Your choice: ").strip().upper()
if choice == "A":
    with open("quiz.txt", "r") as f:
         question = f.readlines()
elif choice == "C":
    with open("popculture.txt", "r") as f:
        question = f.readlines()          
elif choice == "B":
    with open("science.txt", "r") as f:
        question = f.readlines()
while choice not in ["A", "C", "B"]:
        print("Invalid choice. Please choose again.")
        choice = input("Your choice: ").strip().upper()
        if choice == "A":
            with open("quiz.txt", "r") as f:
                question = f.readlines()
                break
        elif choice == "C":
            with open("popculture.txt", "r") as f:
                question = f.readlines()
                break
        elif choice == "B":
            with open("science.txt", "r") as f:
                question = f.readlines()
                break
     
i = 0 
while i + 5 < len(question):
    ques = question[i].strip()
    cho_a = question[i+1].strip()
    cho_b = question[i+2].strip()
    cho_c = question[i+3].strip()
    cho_d = question[i+4].strip()
    ans = question[i+5].strip()
    questions.append({
        "question": ques,
        "choices": [cho_a, cho_b, cho_c, cho_d],
        "answer": ans
    })
    i += 6

random.shuffle(questions)
score = 0 
attempts = 0

for quest in questions:
    print(quest["question"])
    for choice in quest["choices"]:
        print(choice)
    user_choice = input("Your answer: ").strip().upper()
    print()
    if user_choice == quest["answer"]:
        print("Correct")
        print()
        score += 1
        attempts += 1
    elif user_choice == "X":
        print(f"Your score is {score}/{attempts}")
        break
    else:
        print(f"Oops, incorrect, the answer is {quest['answer']}") 
        print()
        attempts += 1   

print(f"Your score is {score}/{attempts}")