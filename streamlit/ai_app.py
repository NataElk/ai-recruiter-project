import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from whatsapp_style import apply_whatsapp_style
from app.agents.main_agent import main_agent

st.set_page_config(page_title="AI Recruiter", layout="centered")
apply_whatsapp_style()

st.markdown('<div class="header">AI Recruiter Chat</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        (
            "assistant",
            "Hi! I'm the AI Recruiter at our Tech company 👋\n\nWe are currently looking for a Python Developer to join our team. In this role, you'll work on building high-quality software solutions, developing data pipelines, and collaborating with cross-functional teams on innovative projects.\n\nHow can I assist you today?"
        )
    ]

if "last_offered_slots" not in st.session_state:
    st.session_state.last_offered_slots = []

if "booked_slot" not in st.session_state:
    st.session_state.booked_slot = None

for role, msg in st.session_state.messages:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(msg)

user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    response, offered_slots, booked_slot = main_agent(
        user_input,
        st.session_state.messages,
        st.session_state.last_offered_slots,
        st.session_state.booked_slot
    )

    st.session_state.last_offered_slots = offered_slots

    if booked_slot is not None:
        st.session_state.booked_slot = booked_slot

    st.session_state.messages.append(("assistant", response))

    with st.chat_message("assistant"):
        st.markdown(response)