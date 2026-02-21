def ask_question(question,options,correct_answer):
    print(f"\n{question}")
    for i,option in enumerate(options,1):
        print(f"{i}.{option}")

    try:
        answer=int(input("Your answer (1-4):"))
        if 1<=answer<=4:
            if options[answer-1]==correct_answer:
                print(f"Correct answer")
                return True
            else:
                print(f"Wrong answer!And Correct answer is:{correct_answer}")
                return False
        else:
            print("Invalid Choice!")
            return False
    except:
        print("Invalid Choice!")
        return False
    
def display_score(correct,total):
    percentage=(correct/total)*100
    print(f"\n{'='*40}")
    print(f"Final Score:{correct}/{total} (Percentage:{percentage})")
    print(f"\n{'='*40}")
    if percentage >= 80:
        print("EXCELLENT! You're a genius!")
    elif percentage >= 60:
        print("GOOD JOB! Keep learning!")
    elif percentage >= 40:
        print("AVERAGE. Study more!")
    else:
        print("POOR. Need more practice!")

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who created Python?",
        "options": ["Bill Gates", "Guido van Rossum", "Elon Musk", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What year did India gain independence?",
        "options": ["1945", "1947", "1950", "1952"],
        "answer": "1947"
    },
    {
        "question": "What is the full form of HTTP?",
        "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol", 
                   "Home Tool Transfer Protocol", "Hyperlink Text Protocol"],
        "answer": "HyperText Transfer Protocol"
    }
]

print("=== QUIZ GAME ===")
print(f"Answer {len(questions)} questions!\n")

score = 0
for q in questions:
    if ask_question(q['question'],q['options'],q['answer']):
        score+=1

display_score(score,len(questions))


    
    