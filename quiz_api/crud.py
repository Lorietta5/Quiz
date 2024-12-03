import logging
from sqlalchemy.orm import Session

from . import models, schemas


# ------------------------ Questions ------------------------

def get_questions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Question).offset(skip).limit(limit).all()


def get_question_by_id(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def update_question(db: Session, question_id: int, question: schemas.QuestionUpdate):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not db_question:
        return None
    for key, value in question.dict(exclude_unset=True).items():
        setattr(db_question, key, value)
    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not db_question:
        return None
    db.delete(db_question)
    db.commit()
    return db_question


# ------------------------ Answers ------------------------
def get_answers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Answer).offset(skip).limit(limit).all()


def get_answer_by_id(db: Session, answer_id: int):
    answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if answer:
        logging.info("Found answer: {answer}")
    else:
        logging.warning(f"Answer with ID {answer_id} not found.")
    return answer


def create_answer(db: Session, answer: schemas.AnswerCreate):
    db_answer = models.Answer(**answer.dict())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def update_answer(db: Session, answer_id: int, answer: schemas.AnswerUpdate):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not db_answer:
        return None
    for key, value in answer.dict(exclude_unset=True).items():
        setattr(db_answer, key, value)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def delete_answer(db: Session, answer_id: int):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not db_answer:
        return None
    db.delete(db_answer)
    db.commit()
    return db_answer
