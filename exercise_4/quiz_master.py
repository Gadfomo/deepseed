import time
import json
import os

quiz_data = {
    "Science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 1},
            {"question": "What gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 1},
            {"question": "What is H2O commonly known as?", "options": ["Salt", "Water", "Ammonia", "Hydrogen"], "answer": 1},
            {"question": "Which organ pumps blood?", "options": ["Lungs", "Brain", "Liver", "Heart"], "answer": 3},
            {"question": "Which planet is closest to the sun?", "options": ["Earth", "Venus", "Mercury", "Mars"], "answer": 2},
        ],
        "hard": [
            {"question": "What is the atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
            {"question": "What is the speed of light in vacuum (m/s)?", "options": ["3x10^8", "1.5x10^7", "3x10^6", "1x10^5"], "answer": 0},
            {"question": "Which law explains planetary motion?", "options": ["Newton's Law", "Ohm's Law", "Kepler's Law", "Archimedes' Law"], "answer": 2},
            {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Cytoplasm"], "answer": 1},
            {"question": "Which element has the symbol 'Fe'?", "options": ["Lead", "Iron", "Fluorine", "Zinc"], "answer": 1},
        ]
    },
    "History": {
        "easy": [
            {"question": "Who was the first President of the USA?", "options": ["Lincoln", "Jefferson", "Washington", "Adams"], "answer": 2},
            {"question": "What year did World War II end?", "options": ["1940", "1942", "1945", "1950"], "answer": 2},
            {"question": "Where were the pyramids built?", "options": ["Mexico", "India", "Egypt", "China"], "answer": 2},
            {"question": "What ship sank in 1912?", "options": ["Olympic", "Lusitania", "Britannic", "Titanic"], "answer": 3},
            {"question": "Who discovered America?", "options": ["Magellan", "Columbus", "Vespucci", "Cook"], "answer": 1},
        ],
        "hard": [
            {"question": "Which treaty ended WWI?", "options": ["Treaty of Paris", "Treaty of Versailles", "Treaty of Rome", "Treaty of Ghent"], "answer": 1},
            {"question": "When did the French Revolution begin?", "options": ["1789", "1776", "1812", "1804"], "answer": 0},
            {"question": "Who was the longest-reigning British monarch before Elizabeth II?", "options": ["George III", "Queen Victoria", "Edward VII", "Henry VIII"], "answer": 1},
            {"question": "Which empire was ruled by Genghis Khan?", "options": ["Ottoman", "Roman", "Mongol", "Persian"], "answer": 2},
            {"question": "Who led India to independence?", "options": ["Nehru", "Patel", "Gandhi", "Bose"], "answer": 2},
        ]
    },
    "Sports": {
        "easy": [
            {"question": "How many players in a football team?", "options": ["9", "10", "11", "12"], "answer": 2},
            {"question": "What sport uses a bat and ball?", "options": ["Soccer", "Basketball", "Cricket", "Hockey"], "answer": 2},
            {"question": "What is a slam dunk in?", "options": ["Tennis", "Basketball", "Football", "Golf"], "answer": 1},
            {"question": "Which sport uses a racket?", "options": ["Rugby", "Tennis", "Hockey", "Boxing"], "answer": 1},
            {"question": "Where are the Olympics held every 4 years?", "options": ["Country", "Continent", "City", "State"], "answer": 2},
        ],
        "hard": [
            {"question": "Which country won the 2018 FIFA World Cup?", "options": ["Brazil", "Germany", "France", "Croatia"], "answer": 2},
            {"question": "How many Grand Slams has Roger Federer won?", "options": ["17", "18", "19", "20"], "answer": 3},
            {"question": "Which sport uses a pommel horse?", "options": ["Swimming", "Gymnastics", "Fencing", "Boxing"], "answer": 1},
            {"question": "What is the maximum break in snooker?", "options": ["147", "155", "170", "200"], "answer": 0},
            {"question": "In which sport is the Davis Cup awarded?", "options": ["Badminton", "Tennis", "Cricket", "Golf"], "answer": 1},
        ]
    }
}

def choose_category_and_difficulty(quiz_data):
    print("=== QUIZ MASTER ===")
    print("Available Categories:")
    for index, category in enumerate(quiz_data.keys(), 1):
        print(f"{index}. {category}")

    while True:
        try:
            cat_choice = int(input("Choose a category (enter number): ")) - 1
            category = list(quiz_data.keys())[cat_choice]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    difficulties = ["easy", "hard"]
    print("\nDifficulties:\n1. Easy\n2. Hard")
    while True:
        try:
            diff_choice = int(input("Choose a difficulty (enter number): ")) - 1
            difficulty = difficulties[diff_choice]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\n📚 Selected: {category} ({difficulty.title()})\n")
    return category, difficulty

def ask_questions(quiz_data, category, difficulty):
    questions = quiz_data[category][difficulty]
    score = 0
    correct_answers = 0
    detailed_results = []
    total = len(questions)

    for index, q in enumerate(questions, 1):
        print(f"Question {index}/{total}: {q['question']}")
        for i, option in enumerate(q['options']):
            print(f"{chr(65 + i)}) {option}")

        start_time = time.time()
        while True:
            answer = input("Your answer (A, B, C, D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Choose A, B, C, or D.")
        end_time = time.time()

        selected_index = ord(answer) - 65
        time_taken = round(end_time - start_time, 2)

        if selected_index == q['answer']:
            print(f"Correct! (+20 points)")
            score += 20
            correct_answers += 1
            is_correct = True
        else:
            print(f"Incorrect! Correct answer: {chr(65 + q['answer'])}) {q['options'][q['answer']]}")
            is_correct = False

        detailed_results.append({
            "question": q['question'],
            "your_answer": answer,
            "correct_answer": chr(65 + q['answer']),
            "is_correct": is_correct,
            "time": time_taken
        })

        print(f"Time: {time_taken} seconds")
        progress = int((index / total) * 10)
        print(f"[{'█' * progress}{'░' * (10 - progress)}] {int((index / total) * 100)}% Complete\n")

    return score, correct_answers, detailed_results

# ===================== SHOW RESULTS =====================
def show_results(score, correct_answers, detailed_results):
    total = len(detailed_results)
    print("\n🎉 QUIZ COMPLETE!")
    print(f"FINAL SCORE: {score}/100")
    print(f"Correct Answers: {correct_answers}/{total}\n")

    print(" DETAILED FEEDBACK:")
    for i, result in enumerate(detailed_results, 1):
        status = "✅" if result["is_correct"] else "❌"
        print(f"{status} Q{i}: {result['question']}")
        print(f"   Your answer: {result['your_answer']}")
        print(f"   Correct answer: {result['correct_answer']}")
        print(f"   Time: {result['time']}s\n")

    if correct_answers == total:
        print("🏆 PERFECT SCORE! You're a quiz master!")
    elif score >= 80:
        print("👏 Great job! You nailed it.")
    elif score >= 50:
        print("👍 Not bad! Keep practicing.")
    else:
        print("💡 Keep trying! Review and come back stronger.")

# ===================== MAIN =====================
if __name__ == "__main__":
    category, difficulty = choose_category_and_difficulty(quiz_data)
    score, correct_answers, detailed_results = ask_questions(quiz_data, category, difficulty)
    show_results(score, correct_answers, detailed_results)
