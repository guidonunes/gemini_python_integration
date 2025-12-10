import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

FLASH_MODEL = "gemini-2.5-flash"
PRO_MODEL = "gemini-2.5-pro"

# Pricing per 1 million tokens
ENTRY_COST_FLASH = 0.30
OUTPUT_COST_FLASH = 2.50

# Pricing per 1 million tokens
ENTRY_COST_PRO = 1.25
OUTPUT_COST_PRO= 10.00


model_flash = genai.get_model(f"models/{FLASH_MODEL}")

flash_model_limits = {
    "input_tokens": model_flash.input_token_limit,
    "output_tokens": model_flash.output_token_limit
}

model_pro = genai.get_model(f"models/{PRO_MODEL}")

pro_model_limits = {
    "input_tokens": model_pro.input_token_limit,
    "output_tokens": model_pro.output_token_limit
}

print(f"Flash Model Token Limits: {flash_model_limits}")
print(f"Pro Model Token Limits: {pro_model_limits}")

llm_flash= genai.GenerativeModel(
    f"models/{FLASH_MODEL}"
    )

tokens_amount = llm_flash.count_tokens("What is the capital of France?")
print(f"Tokens used in the prompt: {tokens_amount}")

response = llm_flash.generate_content("Who won the FIFA World Cup in 2022?")
tokens_prompt = response.usage_metadata.prompt_token_count
tokens_response = response.usage_metadata.candidates_token_count

total_cost = (tokens_prompt / 1_000_000) * ENTRY_COST_FLASH + (tokens_response / 1_000_000) * OUTPUT_COST_FLASH
print(f"total cost of the request: ${total_cost:.6f}")

total_cost_pro = (tokens_prompt / 1_000_000) * ENTRY_COST_PRO + (tokens_response / 1_000_000) * OUTPUT_COST_PRO
print(f"total cost of the request using Pro model: ${total_cost_pro:.6f}")
