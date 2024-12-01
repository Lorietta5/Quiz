from sqlalchemy.orm import Session
from quiz_api.models import Question, Answer
from quiz_api.database import SessionLocal


# noinspection PyGlobalUndefined
def add_multiple_questions_and_answers(db: Session, question=None):

    questions_data = [
        {

            "question_text": "What is the capital of Guinea?",
            "options": ["Conakry", "Bissau", "Algiers", "Cairo"],
            "correct_answer": "Conakry",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
            "question_text": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Venus", "Jupiter"],
            "correct_answer": "Mars",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 2,
        },
        {
            "question_text": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
            "correct_answer": "Pacific",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
            "question_text": "What is the longest river on Earth?",
            "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
            "correct_answer": "Amazon",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
            "question_text": "What is the largest planet in THE Solar system?",
            "options": ["Saturn", "Mercury", "Jupiter", "Neptune"],
            "correct_answer": "Jupiter",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 2,
        },
        {
            "question_text": "What is the highest mountain on Earth?",
            "options": ["Aconcagua", "Everest", "Elbrus", "Denali"],
            "correct_answer": "Everest",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
            "question_text": "Which planet has the densest atmosphere?",
            "options": ["Jupiter", "Mars", "Mercury", "Venus"],
            "correct_answer": "Venus",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 2,
        },
        {
            "question_text": "What is the largest lake on Earth?",
            "options": ["Caspian Sea", "Baikal", "Michigan", "Ontario"],
            "correct_answer": "Caspian Sea",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
            "question_text": "How many continents are there on the planet?",
            "options": ["10", "6", "8", "7"],
            "correct_answer": "7",
            "difficulty": 1,
            "category_id": 1,
            "subcategory_id": 1,
        },
        {
                "question_text": "How many planets are there in the solar system?",
                "options": ["8", "9", "7", "10"],
                "correct_answer": "8",
                "difficulty": 1,
                "category_id": 1,
                "subcategory_id": 2,
            },
        ]

    for data in questions_data:

        question: Question = Question(
            question_text=data["question_text"],
            option_a=data["options"][0],
            option_b=data["options"][1],
            option_c=data["options"][2],
            option_d=data["options"][3],
            correct_answer=data["correct_answer"],
            difficulty=data["difficulty"],
            category_id=data["category_id"],
            subcategory_id=data["subcategory_id"],
        )
        db.add(question)
        db.commit()
        db.refresh(question)

        answers = [
            Answer(question_id=question.id, text=data["options"][0],
                   is_correct=(data["options"][0] == data["correct_answer"])),
            Answer(question_id=question.id, text=data["options"][1],
                   is_correct=(data["options"][1] == data["correct_answer"])),
            Answer(question_id=question.id, text=data["options"][2],
                   is_correct=(data["options"][2] == data["correct_answer"])),
            Answer(question_id=question.id, text=data["options"][3],
                   is_correct=(data["options"][3] == data["correct_answer"])),
        ]
        db.add_all(answers)
        db.commit()

        db.add_all(answers)

    db.commit()
    db.refresh(question)


if __name__ == "__main__":
    with SessionLocal() as db:
        try:
            add_multiple_questions_and_answers(db)
            print("Data has been successfully added to the database.")
        except Exception as e:
            print(f"Error: {e}")
