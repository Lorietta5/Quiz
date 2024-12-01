from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from quiz_api import crud, models, schemas


def test_create_question():

    db = MagicMock(Session)

    question_data = schemas.QuestionCreate(
        question_text="What is the smallest planet in the Solar System?",
        option_a="Saturn",
        option_b="Mercury",
        option_c="Jupiter",
        option_d="Neptune",
        correct_answer="Mercury",
        difficulty=1,
        category_id=1,
        subcategory_id=2
    )

    mock_question = models.Question(**question_data.dict())
    db.add.return_value = None
    db.refresh.return_value = mock_question

    result = crud.create_question(db=db, question=question_data)
    assert result.question_text == "What is the smallest planet in the Solar System?"
    assert result.correct_answer == "Mercury"
