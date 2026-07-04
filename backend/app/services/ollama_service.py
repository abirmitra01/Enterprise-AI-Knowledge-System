import ollama


def ask_llm(prompt: str):

    response = ollama.chat(

        model="qwen2.5:3b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an Enterprise AI Knowledge Assistant. "
                    "Answer ONLY from the provided context. "
                    "Keep answers concise, factual, and under 80 words. "
                    "Prefer bullet points when possible. "
                    "If the answer is not in the context, reply exactly: "
                    "'I couldn't find that information in the uploaded documents.'"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        options={
            "temperature":0.0,
            "top_p":0.7,
            "repeat_penalty":1.15,
            "num_predict":90,
            "num_ctx":4096
        }

    )

    return response["message"]["content"].strip()