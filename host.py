import random
questions = []

with open("quiz.txt", "r") as f:
    question = f.readlines()

i = 0 
while i < len(question):
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
    else:
        print(f"Oops, incorrect, the answer is {quest['answer']}") 
        print()
        attempts += 1   

print(f"Your score is {score}/{attempts}")