from app.rag.rag_service import build_prompt
from app.services.ollama_service import ask_llm


def ask_question(question):

    prompt, sources = build_prompt(question)

    if prompt is None:

        return {
            "answer": "I couldn't find that information in the uploaded documents.",
            "sources": []
        }

    answer = ask_llm(prompt)

    return {

        "answer": answer,

        "sources": sources

    }