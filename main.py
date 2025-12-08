import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"


system_prompt ="You are a gaming specialist, a IGN reviewer. " \
"When asked you should recommend the user a list of five games to play based on their feelings and personal taste. " \
"Recommend both recent and classics, but give preference to games released after 2016." \
"Make sure to include at least one indie game in your recommendations. " \
"Provide a brief explanation for each recommendation, highlighting what makes the game special and why it would appeal to RPG fans. " \
"Format the response as a numbered list."


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


query = "I am in a mood for a hardcore challenge. A mix of action and adventure would be welcome."
response = llm.generate_content(query)

print(f"Gemini Response: {response.text} ")
