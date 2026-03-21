# import os
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient

# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")

# client = InferenceClient(api_key=HF_TOKEN)

# MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


# def call_llm(prompt: str) -> str:
#     try:
#         response = client.chat.completions.create(
#             model=MODEL_NAME,
#             messages=[
#                 {"role": "system", "content": "You are a helpful DSA tutor."},
#                 {"role": "user", "content": prompt},
#             ],
#             max_tokens=300,
#             temperature=0.3,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"❌ Error: {e}"



import os
from huggingface_hub import InferenceClient

# Get token from environment (works locally + Streamlit Cloud)
HF_TOKEN = os.getenv("HF_TOKEN")

# Safety check (VERY IMPORTANT)
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN not found! Please set it in environment variables or Streamlit secrets.")

# Initialize client
client = InferenceClient(api_key=HF_TOKEN)

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


def call_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful DSA tutor."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error: {e}"