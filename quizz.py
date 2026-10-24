from quiz_logic import is_correct_answer, calculate_percentage


questions = [
    {
        "question": "1. Which Git command is used to download a repository from a remote server to a local machine?",
        "options": ["git clone", "git init", "git pull", "git add"],
        "answer": 1,
    },
    {
        "question": "2. Which command allows a developer to see the differences between modified files and the last commit?",
        "options": ["git diff", "git status", "git clone", "git branch"],
        "answer": 1,
    },
    {
        "question": "3. Which command retrieves and merges changes from the remote repository into the current branch?",
        "options": ["git fetch", "git pull", "git merge", "git commit"],
        "answer": 2,
    },
    {
        "question": "4. Which Git command is used to combine the changes from one branch into another branch?",
        "options": ["git clone", "git add", "git merge", "git log"],
        "answer": 3,
    },
    {
        "question": "5. Which Git command is used to send local commits to a remote repository?",
        "options": ["git pull", "git fetch", "git push", "git clone"],
        "answer": 3,
    },
    {
        "question": "6. Which sequence correctly saves local changes and publishes them to the remote repository?",
        "options": [
            "git push -> git add -> git commit",
            "git add -> git commit -> git push",
            "git commit -> git push -> git add",
            "git add -> git push -> git commit",
        ],
        "answer": 2,
    },
]

print("=" * 65)
print("CSC3324 - GIT QUIZ")
print("=" * 65)
print("Choose the number of the correct answer (1, 2, 3, or 4).\n")

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"  {i}. {option}")

    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            break
        print("Please enter 1, 2, 3, or 4.")

    if is_correct_answer(choice, q["answer"]):
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. Correct answer: {q['options'][q['answer'] - 1]}\n")

print("=" * 65)
print(f"FINAL SCORE: {score}/{len(questions)}")
percentage = calculate_percentage(score, len(questions))
print(f"Percentage: {percentage:.1f}%")
print("=" * 65)