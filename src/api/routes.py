from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.qa_service import answer_question

router = APIRouter()

class QuestionIn(BaseModel):
    question: str

@router.get('/health')
def health():
    return {'status':'ok'}

@router.post('/ask')
def ask(q: QuestionIn):
    try:
        return answer_question(q.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
