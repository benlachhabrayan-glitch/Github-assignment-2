import unittest
from quiz_logic import is_correct_answer, calculate_percentage


class TestQuizLogic(unittest.TestCase):

    def test_correct_answer(self):
        self.assertTrue(is_correct_answer("1", 1))

    def test_incorrect_answer(self):
        self.assertFalse(is_correct_answer("2", 1))

    def test_invalid_answer(self):
        self.assertFalse(is_correct_answer("5", 1))

    def test_zero_score_percentage(self):
        self.assertEqual(calculate_percentage(0, 5), 0.0)

    def test_full_score_percentage(self):
        self.assertEqual(calculate_percentage(5, 5), 100.0)


if __name__ == "__main__":
    unittest.main()
