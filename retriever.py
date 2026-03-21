def retrieve_context(query: str) -> str:
    try:
        with open("dsa_patterns_knowledge_base.txt", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""