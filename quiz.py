import random

SAMPLE_DECK = [
  {"term": "algorithm", "clue": "step-by-step instructions to solve a problem"},
  {"term": "repository", "clue": "Storage location for a project and its revision history"},
  {"term": "variable", "clue": "Named container that stores a value in memory"},
]

def run_quiz(deck):
    questions = deck.copy()
    random.shuffle(questions)
    score = 0

    print("\n--- Vocabulary & Concept Quiz ---")
    for index, item in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {item['clue']}")
        answer = input("Your answer: ").strip().lower()
        if answer == item["term"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Not quite — answer: {item['term']}")

    print(f"\nFinal Score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz(SAMPLE_DECK)
