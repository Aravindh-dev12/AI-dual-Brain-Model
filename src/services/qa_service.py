from src.core.orchestration import Orchestrator

orchestrator = Orchestrator()

def answer_question(question: str) -> dict:
    return orchestrator.answer(question)
