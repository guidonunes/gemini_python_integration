import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"

model_config = {
        "temperature": 2.0,
        "max_output_tokens": 8192,
        "top_p": 0.8,
        "top_k": 64,
        "response_mime_type": "text/plain"
    }

def recommend_games(user_input):
    system_prompt = """
        You are a Gaming Specialist.
        1. ANALYSIS: specific recommendations based on user's feeling (e.g., Sad -> Uplifting/Fun).
        2. CRITERIA: Prioritize post-2016 releases. Include at least one indie game.
        3. CONSTRAINTS: Video games only. If asked for non-video games, politely decline.
        4. INPUTS: Ask for/utilize genres, gameplay styles, favorites, and platform.
        5. FORMAT: Numbered list. Brief, concise explanations.
        """

    llm = genai.GenerativeModel(
        model_name=CHOSEN_MODEL,
        system_instruction=system_prompt,
        generation_config=model_config
        )
    response = llm.generate_content(user_input)
    return response.text

def main():
    query = input("Describe your gaming preferences and feelings (or press Enter to quit): ")

    while query != "":
        print(f"Gemini Response: {recommend_games(query)}")
        query = input("Describe your gaming preferences and feelings (or press Enter to quit): ")


if __name__ == "__main__":
    main()
