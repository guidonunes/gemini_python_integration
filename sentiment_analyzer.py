import os
import google.generativeai as genai
from google.api_core.exceptions import NotFound
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = "gemini-2.5-flash"


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


def sentiment_analizer(game_name, model = "gemini-2.5-flash"):
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

    review_category = "reviews_cozy_sim"
    user_pompt = load(f"data/{review_category}.csv")
    print(f"Sentiment Analysis for {review_category} reviews")

    try:
        llm = genai.GenerativeModel(
            model_name=model,
            system_instruction=system_prompt
        )
        response = llm.generate_content(user_pompt)
        response_text = response.text

        save(f"data/{game_name}_sentiment_analysis.txt", response_text)
    except NotFound as e:
        model = "gemini-2.5-flash"
        print(f"Error in the model name: {e}.")
        sentiment_analizer(game_name, model)


def main():
    games_list = ["God of War", "Hollow Knight", "Stardew Valley"]

    for game in games_list:
        sentiment_analizer(game)

if __name__ == "__main__":
    main()
