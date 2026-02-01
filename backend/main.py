from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(data: ChatRequest):
    user_q = data.question.lower()

    if user_q in ["hi", "hello"]:
        answer = "Hi! I can answer questions about Bangalore."

    elif "where is bangalore located" in user_q:
        answer = "Bangalore is located in the southern part of India, in the state of Karnataka."

    elif "what is bangalore known for" in user_q:
        answer = "Bangalore is known as the Silicon Valley of India, famous for IT companies, startups, and pleasant weather."

    elif "well known it hub" in user_q:
        answer = "Electronic City is one of the most well-known IT hubs in Bangalore."

    elif "how many it hubs" in user_q:
        answer = "Bangalore has multiple IT hubs such as Electronic City, Whitefield, Manyata Tech Park, and Outer Ring Road."

    else:
        answer = "Sorry, I can answer only Bangalore-related questions."

    return {"answer": answer}