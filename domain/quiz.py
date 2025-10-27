from dataclasses import dataclass, field
from typing import List
from .question import Question

@dataclass
class Quiz:
    """Представляет собой один тест (викторину).

    Содержит название и список вопросов.

    Attributes:
        title: Название теста.
        questions: Список вопросов (объекты Question) в тесте.
    """
    title: str
    questions: List[Question] = field(default_factory=list)
