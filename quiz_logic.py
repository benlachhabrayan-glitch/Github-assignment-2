def is_correct_answer(choice, correct_answer):
    if choice not in {"1", "2", "3", "4"}:
        return False

    return int(choice) == correct_answer


def calculate_percentage(score, total_questions):
    if total_questions == 0:
        return 0.0

    return score / total_questions * 100