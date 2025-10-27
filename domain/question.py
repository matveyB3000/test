from dataclasses import dataclass, field
from typing import List

@dataclass
class Answer:
    """Представляет собой один вариант ответа на вопрос.

    Attributes:
        text: Текст варианта ответа.
        is_correct: True, если это правильный ответ.
    """
    text: str
    is_correct: bool = False

@dataclass
class Question:
    """Представляет собой один вопрос с текстом и списком ответов.

    Attributes:
        text: Текст вопроса.
        answers: Список вариантов ответа (объекты Answer).
    """
    text: str
    answers: List[Answer] = field(default_factory=list)
