from fastapi import FastAPI
from pydantic import BaseModel
import orchestrator

# Create the HTTP API.
app = FastAPI(title="AI Architecture Demo")

# Define the request and response shapes.
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

# Return server health without calling Gemini.
@app.get("/health")
async def health():
    return {"status": "healthy"}

# Delegate each question across the orchestrator boundary.
@app.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    answer = await orchestrator.answer_question(request.question)
    return AnswerResponse(answer=answer)