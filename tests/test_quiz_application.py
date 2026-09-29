import json
import tempfile
import unittest
from pathlib import Path

from quiz_application import load_questions, filter_questions, calculate_score


class QuizApplicationTests(unittest.TestCase):
    def setUp(self):
        self.questions = [
            {
                "question": "2 + 2 = ?",
                "options": ["4", "3", "5", "6"],
                "answer": "4",
                "category": "Mathematics",
                "difficulty": "Easy",
            },
            {
                "question": "Python function keyword?",
                "options": ["def", "fun", "function", "define"],
                "answer": "def",
                "category": "Python",
                "difficulty": "Easy",
            },
            {
                "question": "Largest ocean?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean",
                "category": "General Knowledge",
                "difficulty": "Medium",
            },
        ]

    def test_load_questions(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "questions.json"
            path.write_text(json.dumps(self.questions), encoding="utf-8")
            loaded = load_questions(path)
            self.assertEqual(len(loaded), 3)
            self.assertEqual(loaded[0]["answer"], "4")

    def test_filter_by_category(self):
        result = filter_questions(self.questions, "Python", "All")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["category"], "Python")

    def test_filter_by_difficulty(self):
        result = filter_questions(self.questions, "All", "Medium")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["difficulty"], "Medium")

    def test_filter_by_both(self):
        result = filter_questions(self.questions, "Mathematics", "Easy")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["answer"], "4")

    def test_score_calculation(self):
        selected = {0: "4", 1: "wrong", 2: "Pacific Ocean"}
        self.assertEqual(calculate_score(self.questions, selected), 2)

    def test_invalid_question_file(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            path.write_text(
                json.dumps([{
                    "question": "Bad question",
                    "options": ["A", "B", "C"],
                    "answer": "A",
                    "category": "Test",
                    "difficulty": "Easy",
                }]),
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                load_questions(path)


if __name__ == "__main__":
    unittest.main()
