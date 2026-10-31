from model_provider import generate
from architecture_context import load_architecture

# Add the same system context to every user question.
SYSTEM_CONTEXT = "You are a helpful assistant. Respond concisely."

# Build the prompt before delegating the async model call.
async def answer_question(user_question: str) -> str:
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {user_question}"
    return await generate(prompt)

# Ground architecture answers in the current Mermaid diagram.
async def answer_architecture_question(user_question: str) -> str:
    architecture = load_architecture()
    prompt = (
        "Answer only from this C4 architecture. "
        f"Architecture:\n{architecture}\n\nQuestion: {user_question}"
    )
    return await generate(prompt)