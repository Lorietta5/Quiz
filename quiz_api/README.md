1. Project title:
# Quiz_API
2. Brief description of the project:
Quiz API - This is an API for managing quiz questions and answers. It supports CRUD operations on questions and answers, and also allows you to integrate the functionality into your applications.
3. Functionality:
List of key project capabilities:
- Add new questions and answers.
- Get a list of questions or answers.
- Update existing data.
- Delete questions or answers.
4.Technologies:
List of technologies used in the project:
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
5. How to install a project:
Step-by-step instructions:
### Cloning a repository
git clone https://github.com/Lorietta5/Quiz.git

### Formation of dependencies
cd quiz_api
pip install -r requirements.txt

### Launching the API
You can run the project using the following command:
uvicorn main:app --reload

6.How to use
Swagger UI link and Postman usage example:
### Swagger UI
API is available at: http://127.0.0.1:8001/docs

## Add the Following Endpoints
- Endpoint to Create a New Question: POST /questions/{question_id}
- Endpoint to Create a New Answer: POST /answers/{answers_id}
- Endpoint to Get Questions: GET /questions/{question_id}
- Endpoint to Get Answers: GET /answers/{answer_id} her
- Endpoint to Delete a Answers: DELETE /answers/{answer_id}
- Endpoint to Delete a Questions: DELETE /questions/{question_id}

### Postman query example
You can find the Postman collection in the file `postman_collection.json` at the root of the project.
Database schema:
-"questions" (id,question_text,answer options, correct_answer, difficulty, category_id, subcategory_id)
-"answers" (ID, question_id, text, is_correct)
-"subcategories" (id, name)
-"categories" (id, name)


    



