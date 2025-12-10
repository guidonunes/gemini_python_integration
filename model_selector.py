import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = "gemini-2.5-flash"


def load (file_path):
    try:
        with open (file_path, 'r') as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Error: {e}.")

system_prompt = """
Identify the gaming profile for each gamer below based on their equipment and habits.

The output format must be:
gamer - describe the gamer's profile in 3 words
"""


user_prompt = load("data/data.csv")

flash_model = genai.GenerativeModel(f"models/{model}")
token_count = flash_model.count_tokens(user_prompt)

TOKEN_LIMIT = 8192


if token_count.total_tokens > TOKEN_LIMIT:
    model = "gemini-2.5-pro"

print(f"Using model: {model}")

llm = genai.GenerativeModel(
    model_name=model,
    system_instruction=system_prompt
)


response = llm.generate_content(user_prompt)

print(f"Response: {response.text}")
