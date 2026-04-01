from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are a software performance optimization expert.

Given a piece of code:
- Identify inefficiencies
- Suggest improvements
- Optimize for performance and readability
- Explain reasoning clearly
"""

def optimize_code(code: str) -> str:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Optimize this code:\n{code}"}
        ],
    )
    return response.output_text