import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"


def load(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Error: {e}.")


def save(file_path, content):
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error: {e}.")

system_prompt = f"""
You are a sentiment analyzer for video game reviews.
Write a paragraph of up to 50 words summarizing the reviews and then attribute the general sentiment for the game or genre.
Also identify 3 strengths and 3 weaknesses identified from the reviews.

# Output Format

Game/Genre Name:
Review Summary:
General Sentiment: [use only Positive, Negative, or Neutral]
Strengths: list with three bullets
Weaknesses: list with three bullets
"""
