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
import requests
import streamlit as st

print("SECRETS:", st.secrets)
#HF_TOKEN = os.getenv("HF_TOKEN")
HF_TOKEN = st.secrets["HF_TOKEN"]
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found!")

API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def call_llm(prompt: str) -> str:
    try:
        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": 0.3,
                "max_new_tokens": 300
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        result = response.json()

        if isinstance(result, list):
            return result[0]["generated_text"]

        return str(result)

    except Exception as e:
        return f"❌ Error: {e}"