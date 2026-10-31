from model_provider import generate

# Add the same system context to every user question.
SYSTEM_CONTEXT = "You are a helpful assistant. Respond concisely."

# Build the prompt before delegating the async model call.
async def answer_question(user_question: str) -> str:
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {user_question}"
    return await generate(prompt)