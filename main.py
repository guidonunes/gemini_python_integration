import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"


system_prompt ="You are a gaming specialist. When asked you should recommend the user a list of three games to play based on their feelings and personal taste. Recommend both recent and classics, but give preference to games released after 2016."


model_config = {
    "temperature": 2.0,
    "max_output_tokens": 8192,
    "top_p": 0.8,
    "top_k": 64,
    "response_mime_type": "text/plain"
}

llm = genai.GenerativeModel(
    model_name=CHOSEN_MODEL,
    system_instruction=system_prompt,
    generation_config=model_config
    )


query = "list 3 video games that every rpg fan should play."
response = llm.generate_content(query)

print(f"Gemini Response: {response.text} ")
