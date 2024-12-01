import logging

from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from quiz_api import crud, schemas
from quiz_api.database import SessionLocal

# FastAPI settings
app = FastAPI(
    title="Quiz_API",
    description="API for quiz management: create, edit, view, and delete questions and answers.",
    version="1.0.0"
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom Quiz API",
        version="1.0.0",
        description="Custom OpenAPI schema for the Quiz API",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Dependency for database session


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------ Questions ------------------------

@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    """
            Create a new question.
            """
    return crud.create_question(db=db, question=question)


@app.get("/questions/", response_model=list[schemas.Question])
def read_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
        Get all questions with optional pagination.
        """
    return crud.get_questions(db, skip=skip, limit=limit)


@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    """
            Find a question by id.
            """
    question = crud.get_question_by_id(db=db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@app.put("/questions/{question_id}", response_model=schemas.Question)
def update_question(question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    """
            Update a question by id.
            """
    updated_question = crud.update_question(db=db, question_id=question_id, question=question)
    if not updated_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return updated_question


@app.delete("/questions/{question_id}", response_model=dict)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """
            Delete a question by id.
            """
    deleted_question = crud.delete_question(db=db, question_id=question_id)
    if not deleted_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": f"Question with ID {question_id} deleted successfully"}


# ------------------------ Answers ------------------------

@app.post("/answers/", response_model=schemas.Answer)
def create_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    logging.info(f"Received answer: {answer}")
    """
        Create a new answer.
        """
    return crud.create_answer(db=db, answer=answer)


@app.get("/answers/", response_model=list[schemas.Answer])
def read_answers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
        Get all answers with optional pagination.
        """
    return crud.get_answers(db, skip=skip, limit=limit)


@app.get("/answers/{answer_id}", response_model=schemas.Answer)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    """
                    Find an answer by id.
                    """
    answer = crud.get_answer_by_id(db=db, answer_id=answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer


@app.put("/answers/{answer_id}", response_model=schemas.Answer)
def update_answer(answer_id: int, answer: schemas.AnswerUpdate, db: Session = Depends(get_db)):
    """
                    Update an answer by id.
                    """
    updated_answer = crud.update_answer(db=db, answer_id=answer_id, answer=answer)
    if not updated_answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return updated_answer


@app.delete("/answers/{answer_id}", response_model=dict)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    """
                    Delete an answer by id.
                    """
    deleted_answer = crud.delete_answer(db=db, answer_id=answer_id)
    if not deleted_answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"message": f"Answer with ID {answer_id} deleted successfully"}
