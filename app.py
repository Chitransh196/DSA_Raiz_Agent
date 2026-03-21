# import streamlit as st
# from orchestrator import run_agent
# from conversation_memory import clear_memory

# st.set_page_config(page_title="DSA Practice Buddy", page_icon="🤖")

# st.title("🤖 DSA Practice Buddy")
# st.write("Ask a DSA question, get pattern hints, run code, or ask for a recommendation.")

# if st.button("Clear Memory"):
#     clear_memory()
#     st.success("Memory cleared!")

# user_input = st.text_area("Ask your question:", height=150)

# if st.button("Submit"):
#     if user_input.strip():
#         with st.spinner("Thinking..."):
#             response = run_agent(user_input)
#         st.write(response)
#     else:
#         st.warning("Please enter a question.")






# import streamlit as st
# from orchestrator import run_agent
# from conversation_memory import clear_memory

# # --------- Page Config ---------
# st.set_page_config(
#     page_title="DSA Raiz Agent",
#     page_icon="🤖",
#     layout="centered"
# )

# # --------- Custom Blue + Silver Theme ---------
# st.markdown("""
# <style>

# /* Main background */
# .stApp {
#     background-color: #0B1F3A;
#     color: #E5E7EB;
# }

# /* Title */
# h1 {
#     color: #60A5FA;
# }

# /* Chat bubbles */
# .stChatMessage {
#     border-radius: 12px;
#     padding: 10px;
# }

# /* User message bubble */
# [data-testid="stChatMessage-user"] {
#     background-color: #1E3A5F;
# }

# /* Assistant message bubble */
# [data-testid="stChatMessage-assistant"] {
#     background-color: #2E2E2E;
# }

# /* Chat input */
# .stChatInput input {
#     background-color: #1F2937;
#     color: #E5E7EB;
# }

# /* Buttons */
# .stButton button {
#     background-color: #3B82F6;
#     color: white;
#     border-radius: 8px;
#     border: none;
# }

# /* Button hover */
# .stButton button:hover {
#     background-color: #2563EB;
# }

# /* Sidebar (if used later) */
# section[data-testid="stSidebar"] {
#     background-color: #111827;
# }

# </style>
# """, unsafe_allow_html=True)

# # --------- Title ---------
# st.title("🤖 DSA Raiz Agent")
# st.caption("Ask DSA questions, get hints, run code, or request problems 🚀")

# # --------- Clear Memory Button ---------
# col1, col2 = st.columns([1, 5])
# with col1:
#     if st.button("🧹 Clear"):
#         clear_memory()
#         st.success("Memory cleared!")

# # --------- Chat State ---------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --------- Display Previous Messages ---------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# # --------- Chat Input ---------
# user_input = st.chat_input("Ask your question...")

# if user_input:
#     # Show user message
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input
#     })
#     with st.chat_message("user"):
#         st.write(user_input)

#     # Generate response
#     with st.spinner("Thinking..."):
#         response = run_agent(user_input)

#     # Show bot response
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response
#     })
#     with st.chat_message("assistant"):
#         st.write(response)



import streamlit as st
from orchestrator import run_agent
from conversation_memory import clear_memory

# --------- Page Config ---------
st.set_page_config(
    page_title="DSA Raiz Agent",
    page_icon="🤖",
    layout="centered"
)

# --------- Custom CSS (Blue + Silver + Tribal Background) ---------
st.markdown("""
<style>

/* Main background with tribal design */
.stApp {
    background: linear-gradient(rgba(11,31,58,0.90), rgba(11,31,58,0.95)),
                url("https://images.unsplash.com/photo-1549887534-1541e9326642");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #E5E7EB;
}

/* Title styling */
h1 {
    color: #60A5FA;
    text-align: center;
}

/* Subtitle */
.stCaption {
    text-align: center;
    color: #9CA3AF;
}

/* Chat bubbles */
.stChatMessage {
    border-radius: 12px;
    padding: 10px;
    backdrop-filter: blur(6px);
}

/* User message */
[data-testid="stChatMessage-user"] {
    background-color: rgba(30, 58, 95, 0.85);
}

/* Assistant message */
[data-testid="stChatMessage-assistant"] {
    background-color: rgba(46, 46, 46, 0.85);
}

/* Chat input */
.stChatInput input {
    background-color: rgba(31, 41, 55, 0.9);
    color: #E5E7EB;
}

/* Buttons */
.stButton button {
    background-color: #3B82F6;
    color: white;
    border-radius: 8px;
    border: none;
}

/* Button hover */
.stButton button:hover {
    background-color: #2563EB;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #3B82F6;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------- Title ---------
st.title("🤖 DSA Raiz Agent")
st.caption("Ask DSA questions, get hints, run code, or request problems 🚀")

# --------- Clear Memory Button ---------
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🧹 Clear"):
        clear_memory()
        st.success("Memory cleared!")

# --------- Chat State ---------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------- Display Previous Messages ---------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --------- Chat Input ---------
user_input = st.chat_input("Ask your question...")

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.spinner("Thinking..."):
        response = run_agent(user_input)

    # Show assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)