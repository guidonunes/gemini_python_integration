import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

CHOSEN_MODEL = "gemini-2.5-flash"

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


query = "The games are: The Witcher 3, Celeste, Doom Eternal, Stardew Valley, Dark Souls III."
response = llm.generate_content(query)


print(f"Gemini Response: {response.text} ")
