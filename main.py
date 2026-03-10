import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from gradient_adk import entrypoint, RequestContext, trace_llm

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

@trace_llm(name="grok_inference")
async def call_grok(prompt: str) -> str:
    completion = await client.responses.create(
        model="grok-4-1-fast-reasoning",  # Recommended 2026 model – check https://docs.x.ai/developers/models
        input=[
            {"role": "system", "content": "You are Grok, a helpful and maximally truthful AI built by xAI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return completion.output_text

@entrypoint
async def main(payload: dict, context: RequestContext):
    user_prompt = payload.get("prompt") or payload.get("query") or "Hello from Grok on DigitalOcean!"
    response = await call_grok(user_prompt)
    return {"response": response}
