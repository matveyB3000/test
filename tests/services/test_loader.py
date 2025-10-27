import unittest
import json
import os
from domain.quiz import Quiz
from domain.question import Question, Answer
from services.quiz_loader import Loader

class TestLoader(unittest.TestCase):

    def setUp(self):
        self.loader = Loader()
        self.quiz = Quiz(
            title="math",
            questions=[
                Question(
                    text="2+2?",
                    answers=[
                        Answer(text="4", is_correct=True),
                        Answer(text="5", is_correct=False)
                    ]
                )
            ]
        )
        self.test_file = "test_quiz.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        self.loader.save(self.test_file, self.quiz)
        loaded_quiz = self.loader.load(self.test_file)
        self.assertEqual(self.quiz, loaded_quiz)

if __name__ == '__main__':
    unittest.main()