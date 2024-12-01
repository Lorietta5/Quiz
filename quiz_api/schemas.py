from typing import List, Optional
from pydantic import BaseModel

# -------------------- Base Schemas --------------------


class QuestionBase(BaseModel):
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    difficulty: int
    category_id: int
    subcategory_id: int

    class Config:
        from_attributes = True  # Enable ORM compatibility


class AnswerBase(BaseModel):
    question_id: int
    text: str
    is_correct: bool

    class Config:
        from_attributes = True  # Enable ORM compatibility

# -------------------- Create Schemas --------------------


class QuestionCreate(QuestionBase):
    pass


class AnswerCreate(AnswerBase):
    pass


# -------------------- Update Schemas --------------------


class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_answer: Optional[str] = None
    difficulty: Optional[int] = None
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None

    class Config:
        from_attributes = True


class AnswerUpdate(BaseModel):
    question_id: int
    text: str
    is_correct: bool

    class Config:
        from_attributes = True

# -------------------- Response Schemas --------------------


class Answer(BaseModel):
    id: int
    question_id: int
    text: str
    is_correct: bool

    class Config:
        from_attributes = True


class Question(BaseModel):
    id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    difficulty: int
    category_id: int
    subcategory_id: int
    answers: List[Answer] = []

    class Config:
        from_attributes = True
