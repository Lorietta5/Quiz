import pytest
from fastapi.testclient import TestClient

from quiz_api import models
from quiz_api.database import SessionLocal, engine
from quiz_api.main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def test_db():

    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        models.Base.metadata.drop_all(bind=engine)


def test_create_question_api(test_db):
    question_data = {
        "question_text": "What is the smallest planet in the Solar System?",
        "option_a": "Saturn",
        "option_b": "Mercury",
        "option_c": "Jupiter",
        "option_d": "Neptune",
        "correct_answer": "Mercury",
        "difficulty": 1,
        "category_id": 1,
        "subcategory_id": 2
    }

    response = client.post("/questions/", json=question_data)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["question_text"] == "What is the smallest planet in the Solar System?"
    assert response_data["correct_answer"] == "Mercury"


def test_read_question_api(test_db):
    question_data = {
        "question_text": "What is the smallest planet in the Solar System?",
        "option_a": "Saturn",
        "option_b": "Mercury",
        "option_c": "Jupiter",
        "option_d": "Neptune",
        "correct_answer": "Mercury",
        "difficulty": 1,
        "category_id": 1,
        "subcategory_id": 2
    }

    response = client.post("/questions/", json=question_data)
    question_id = response.json()["id"]

    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == question_id
    assert response_data["question_text"] == "What is the smallest planet in the Solar System?"
