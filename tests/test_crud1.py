from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from quiz_api import crud, models


def test_delete_answer():

    db = MagicMock(Session)

    mock_answer = models.Answer(id=1, text="Mercury", is_correct=True, question_id=1)

    db.query.return_value.filter.return_value.first.return_value = mock_answer
    db.delete.return_value = None
    db.commit.return_value = None

    result = crud.delete_answer(db=db, answer_id=1)

    assert result.id == 1
    assert result.text == "Mercury"

    db.delete.assert_called_once_with(mock_answer)
    db.commit.assert_called_once()
