from openai import OpenAI

from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(conversation: list) -> str:
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="""
        You are a helpful software engineering assistant.
        Answer clearly and concisely.
        """,
        input=conversation
    )
    return response.output_text