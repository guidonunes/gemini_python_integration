import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"


system_prompt ="list five famous video games from the 1990s in a numbered format."

llm = genai.GenerativeModel(
    model_name=CHOSEN_MODEL,
    system_instruction=system_prompt
    )


query = "list 3 video games that every rpg fan should play."
response = llm.generate_content(query)

print(f"Gemini Response: {response.text} ")
