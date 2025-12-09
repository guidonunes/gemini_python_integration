import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"


def categorize_games(title, possible_genres):
    system_prompt = f"""You should categorize the games that user provides into their respective genres.{possible_genres}
        #Fomat
        Game: Name of the Game
        Genre: Category

        #Example
        Game: The Legend of Zelda: Breath of the Wild
        Genre: Adventure
    """

    llm = genai.GenerativeModel(
        model_name=CHOSEN_MODEL,
        system_instruction=system_prompt
    )

    response = llm.generate_content(title)
    return response.text


def main():
    possible_genres = [
        "Action",
        "Adventure",
        "Role-Playing",
        "Simulation",
        "Strategy",
        "Sports",
        "Puzzle",
        "Idle",
        "Horror",
        "Platformer",
        "Shooter",
        "Fighting",
        "Racing",
        "MMORPG",
        "Survival",
        "Stealth"
    ]

    query = "The games are: The Witcher 3, Celeste, Doom Eternal, Stardew Valley, Dark Souls III."
    print(f"Response: {categorize_games(query, possible_genres)}")

if __name__ == "__main__":
    main()
