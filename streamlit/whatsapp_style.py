import html
import streamlit as st


def apply_whatsapp_style():
    st.markdown("""
    <style>
    .stApp {
        background-color: #ECE5DD;
    }

    .block-container {
        max-width: 900px;
        padding-top: 120px !important;
        padding-bottom: 7rem;
    }

    .header {
        position: fixed;
        top: 50px;
        left: 0;
        right: 0;
        background: #128C7E;
        color: white;
        padding: 18px;
        font-size: 24px;
        font-weight: 700;
        text-align: center;
        z-index: 999;
    }

    /* ── Remove default background ── */
    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        padding: 4px 0 !important;
        gap: 6px !important;
    }

    /* ── Message content - shared base ── */
    [data-testid="stChatMessageContent"] {
        border-radius: 12px !important;
        padding: 10px 14px !important;
        font-size: 15px !important;
        line-height: 1.5 !important;
        max-width: 70% !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.10) !important;
        color: #111B21 !important;
    }

    /* ── USER: reverse direction + green bubble ── */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row-reverse !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
        background: #DCF8C6 !important;
        border-radius: 12px 12px 0 12px !important;
        margin-right: 0 !important;
    }

    /* ── ASSISTANT: white bubble ── */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {
        background: #FFFFFF !important;
        border-radius: 12px 12px 12px 0 !important;
        margin-left: 0 !important;
    }

    /* ── Input box ── */
    .stChatInputContainer {
        background: #111B21 !important;
        border-top: none !important;
        padding: 12px !important;
    }

    .stChatInputContainer textarea {
        background: white !important;
        border-radius: 24px !important;
        border: 1px solid #D1D7DB !important;
        padding: 10px 14px !important;
        color: #111B21 !important;
    }

    /* ── render_chat (if used) ── */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 16px 0;
    }

    .message-row {
        display: flex;
        width: 100%;
    }

    .message-row.user {
        flex-direction: row-reverse;
    }

    .message-row.assistant {
        flex-direction: row;
    }

    .message-bubble {
        max-width: 70%;
        padding: 10px 14px;
        font-size: 15px;
        line-height: 1.5;
        color: #111B21;
        word-wrap: break-word;
        white-space: pre-wrap;
        box-shadow: 0 1px 1px rgba(0, 0, 0, 0.08);
    }

    .message-row.user .message-bubble {
        background: #DCF8C6;
        border-radius: 12px 12px 0 12px;
    }

    .message-row.assistant .message-bubble {
        background: #FFFFFF;
        border-radius: 12px 12px 12px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def render_chat(messages):
    parts = ['<div class="chat-container">']

    for role, msg in messages:
        safe_msg = html.escape(msg).replace("\n", "<br>")
        role_class = "user" if role == "user" else "assistant"

        parts.append(f"""
        <div class="message-row {role_class}">
            <div class="message-bubble">{safe_msg}</div>
        </div>
        """)

    parts.append("</div>")
    st.markdown("".join(parts), unsafe_allow_html=True)