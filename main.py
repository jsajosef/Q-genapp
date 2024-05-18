from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Question
from pydantic import BaseModel

app = FastAPI()

class QuestionCreate(BaseModel):
    question_text: str

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/questions/")
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = Question(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.get("/questions/")
def read_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions