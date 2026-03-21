# from llm_client import call_llm
# from code_executor import run_code
# from problem_recommender import recommend_problem
# from retriever import retrieve_context
# from conversation_memory import save_memory, get_memory


# def run_agent(user_input: str) -> str:
#     text = user_input.lower()

#     if "```" in user_input:
#         return run_code(user_input)

#     if "recommend" in text:
#         return recommend_problem()

#     memory = get_memory()
#     history = "\n".join(
#         [f"User: {m['user']}\nBot: {m['bot']}" for m in memory[-3:]]
#     )

#     context = retrieve_context(user_input)

#     prompt = f"""
# You are a helpful DSA tutor for beginners.

# Previous conversation:
# {history}

# Reference context:
# {context}

# User question:
# {user_input}

# Instructions:
# - Understand the user's intent using reasoning.
# - Do not depend only on exact words from the reference context.
# - If the question is ambiguous, say the possible interpretations first.
# - If one interpretation matches a common coding interview problem, mention that clearly.
# - Use the reference context only as support, not as the only source.
# - Give a practical answer even if the exact pattern is not explicitly written in the context.
# - If the question is about a simple operation, say that clearly.
# - If the question can map to a known DSA pattern, explain that too.
# - Keep the answer simple and beginner-friendly.
# - Give full code when user asks.

# Answer in this format:

# Possible interpretation:
# ...

# Best pattern to use:
# ...

# Why:
# ...

# Hint:
# ...

# Time complexity target:
# ...
# """

#     answer = call_llm(prompt)
#     save_memory(user_input, answer)
#     return answer

from llm_client import call_llm
from code_executor import run_code
from problem_recommender import recommend_problem
from retriever import retrieve_context
from conversation_memory import save_memory, get_memory


def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    if "```" in user_input:
        return "code"

    if "recommend" in text:
        return "recommend"

    if any(x in text for x in ["structure", "format", "pattern"]):
        return "structured"

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "chat"

    return "normal"


def run_agent(user_input: str) -> str:
    intent = detect_intent(user_input)

    # 🔧 TOOL: Run code
    if intent == "code":
        return run_code(user_input)

    # 🎯 TOOL: Recommend problem
    if intent == "recommend":
        return recommend_problem()

    # 🧠 Memory
    memory = get_memory()
    history = "\n".join(
        [f"User: {m['user']}\nBot: {m['bot']}" for m in memory[-3:]]
    )

    # 📚 Context
    context = retrieve_context(user_input)

    # 🧠 Dynamic Prompt
    if intent == "chat":
        prompt = f"""
You are a friendly AI assistant.

Conversation:
{history}

User:
{user_input}

Respond naturally like ChatGPT.
"""

    elif intent == "structured":
        prompt = f"""
You are a DSA tutor.

Previous conversation:
{history}

Reference context:
{context}

User question:
{user_input}

Answer in this format:

Possible interpretation:
...

Best pattern to use:
...

Why:
...

Hint:
...

Time complexity target:
...
"""

    else:  # normal mode
        prompt = f"""
You are a helpful DSA tutor.

Previous conversation:
{history}

Reference context:
{context}

User question:
{user_input}

Instructions:
- Understand the user's intent.
- Explain clearly and simply.
- Give examples if needed.
- Give code ONLY if user asks.

Answer naturally (not forced format).
"""

    answer = call_llm(prompt)
    save_memory(user_input, answer)
    return answer