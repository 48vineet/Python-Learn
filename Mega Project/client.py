from google import genai

client = genai.Client(api_key="AIzaSyDY0t8Qb4UmQ4oAGxhN-PGboE7pKGh3zKw")

SYSTEM_PROMPT = """
You are Jarvis, a smart personal voice assistant.
You speak like a polite, friendly human assistant.
You give short, clear, natural replies.
You never say you are an AI or language model.
You never give long explanations.
You sound calm, confident, and helpful.
If greeting, greet warmly.
If asked casual questions, respond casually.
Max response length: 1 sentence.
"""


def ask_ai(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\nUser: {prompt}\nJarvis:"
        )
        return response.text.strip()
    except Exception:
        return "Sorry, I had trouble answering that."
