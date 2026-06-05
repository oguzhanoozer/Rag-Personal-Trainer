"""
KINETIC AI - RAG Personal Trainer
HTML tasarımının birebir Streamlit uygulaması
"""

import streamlit as st
import streamlit.components.v1 as components
from simple_test import SimpleRAGTrainer
import os
import html as html_module
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="⚡ Kinetic AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Session state & auto-load ──────────────────────────────────────
if "trainer" not in st.session_state:
    st.session_state.trainer = SimpleRAGTrainer()
    st.session_state.loaded = False
    st.session_state.chat_history = []

if not st.session_state.loaded:
    try:
        st.session_state.trainer.load_knowledge_base()
        st.session_state.loaded = True
    except Exception as e:
        st.error(f"System initialization failed: {e}")

# ── Full-page CSS override ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap');

/* ── Force light color-scheme globally ── */
:root { color-scheme: light !important; }
html { color-scheme: light !important; }
* { color-scheme: light !important; }

/* ── Nuclear: reset ALL backgrounds to light ── */
[data-testid="stApp"],
[data-testid="stApp"] *:not([data-testid="stFormSubmitButton"] button):not([data-testid="stFormSubmitButton"] button *) {
    background-color: transparent !important;
    color: #2c2f32 !important;
}

/* ── Main page background ── */
html, body { background: #f4f6fa !important; }
[data-testid="stApp"] { background: #f4f6fa !important; }
[data-testid="stAppViewContainer"] { background: #f4f6fa !important; }
.main { background: #f4f6fa !important; }
.block-container { background: #f4f6fa !important; }

/* ── Font ── */
[data-testid="stApp"], [data-testid="stApp"] * {
    font-family: 'Inter', sans-serif !important;
}

/* ── White bg elements ── */
.q-box, .a-box, .top-bar,
div[data-testid="column"] .stButton > button,
[data-testid="stForm"],
details, details > summary, details > div,
[data-baseweb] {
    background: #ffffff !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div:first-child {
    background: #eef1f5 !important;
}
.sb-stats { background: rgba(217,221,227,0.5) !important; }

/* hr / divider */
hr { border-color: rgba(0,0,0,0.1) !important; }

/* ── Material Symbols helper ── */
.material-symbols-outlined {
    font-family: 'Material Symbols Outlined' !important;
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    display: inline-block;
    vertical-align: middle;
}
.mso-fill { font-variation-settings: 'FILL' 1, 'wght' 400; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #eef1f5 !important;
    padding: 1.5rem !important;
    width: 320px !important;
    color-scheme: light !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    background-color: #eef1f5 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span,
[data-testid="stSidebar"] hr {
    color: inherit !important;
    background: transparent !important;
}

/* sidebar brand block */
.sb-brand { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 2rem; }
.sb-brand-icon {
    width: 2.5rem; height: 2.5rem; border-radius: 0.5rem;
    background: #b61321; display: flex; align-items: center; justify-content: center; color: #fff;
}
.sb-brand h2 {
    font-family: 'Lexend', sans-serif; font-weight: 700; color: #b61321;
    font-size: 0.875rem; letter-spacing: 0.15em; text-transform: uppercase; margin: 0;
}
.sb-brand p {
    font-size: 0.625rem; color: #595c5f; font-weight: 500; margin: 0;
}

/* sidebar nav */
.sb-nav-item {
    display: flex; align-items: center; gap: 0.75rem;
    padding: 0.75rem 1rem; border-radius: 0.5rem;
    font-family: 'Lexend', sans-serif; font-size: 0.75rem;
    font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em;
    color: #595c5f; cursor: pointer; transition: background 0.2s;
}
.sb-nav-item:hover { background: #e5e8ed; }
.sb-nav-item.active { background: rgba(0,102,102,0.1); color: #006666; }

/* sidebar stats card */
.sb-stats {
    background: rgba(217,221,227,0.5); padding: 1rem; border-radius: 0.75rem;
    margin: 1rem 0;
}
.sb-stats-title {
    font-family: 'Lexend', sans-serif; font-size: 0.625rem; font-weight: 700;
    color: #595c5f; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 1rem;
}
.sb-stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.sb-stats-label { font-size: 0.625rem; color: #595c5f; text-transform: uppercase; }
.sb-stats-value { font-family: 'Lexend', sans-serif; font-weight: 700; color: #006666; font-size: 1.25rem; }
.sb-stats-status {
    margin-top: 0.75rem; display: flex; align-items: center; gap: 0.5rem;
    font-size: 0.625rem; font-weight: 700; color: #006666;
}

/* sidebar footer nav */
.sb-footer-item {
    display: flex; align-items: center; gap: 0.75rem;
    padding: 0.5rem 1rem; border-radius: 0.5rem;
    font-family: 'Lexend', sans-serif; font-size: 0.625rem;
    font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em;
    color: #595c5f; cursor: pointer; transition: background 0.2s;
}
.sb-footer-item:hover { background: #e5e8ed; }

/* ── Top App Bar ── */
.top-bar {
    background: #ffffff; padding: 1rem 2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    display: flex; justify-content: space-between; align-items: center;
    margin: -1rem -1.5rem 0 -1.5rem;
    position: sticky; top: 0; z-index: 10;
}
.top-bar-logo {
    font-family: 'Lexend', sans-serif; font-size: 1.5rem; font-weight: 900;
    color: #006666;
    letter-spacing: -0.02em;
}
.top-nav { display: flex; gap: 2rem; }
.top-nav a {
    font-family: 'Lexend', sans-serif; font-size: 0.875rem; font-weight: 500;
    text-decoration: none; color: #595c5f; padding-bottom: 0.25rem;
    transition: color 0.2s;
}
.top-nav a.active {
    color: #006666; font-weight: 700; border-bottom: 2px solid #006666;
}
.top-nav a:hover { color: #b61321; }
.top-bar-right { display: flex; align-items: center; gap: 1rem; }
.top-bar-right .material-symbols-outlined {
    color: #595c5f; cursor: pointer; transition: color 0.2s;
}
.top-bar-right .material-symbols-outlined:hover { color: #b61321; }
.top-bar-avatar {
    width: 2rem; height: 2rem; border-radius: 9999px; background: #e5e8ed;
}

/* ── Hero section ── */
.hero-title {
    font-family: 'Lexend', sans-serif; font-weight: 900;
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    color: #006666;
    text-align: center; letter-spacing: -0.05em; line-height: 1.1;
    margin: 3rem 0 1rem; padding: 0;
}
.hero-sub {
    text-align: center; color: #595c5f; font-size: 1.25rem;
    font-weight: 300; letter-spacing: 0.02em; margin-bottom: 3rem;
}

/* ── Bento card buttons ── */
div[data-testid="column"] .stButton > button {
    background: #ffffff !important; color: #2c2f32 !important;
    border: 1.5px solid rgba(0,102,102,0.15) !important;
    border-radius: 0.75rem !important;
    padding: 2rem !important; text-align: left !important;
    font-family: 'Lexend', sans-serif !important;
    font-weight: 600 !important; font-size: 1.05rem !important;
    height: 12rem !important; box-shadow: none !important;
    white-space: normal !important; line-height: 1.4 !important;
    transition: all 0.25s ease !important; cursor: pointer !important;
}
div[data-testid="column"] .stButton > button:hover {
    box-shadow: 0 20px 25px -5px rgba(0,102,102,0.08) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="column"] .stButton > button:active {
    transform: scale(0.98) !important;
}

/* ── Floating input area ── */
.floating-bar {
    background: #ffffff; border-radius: 9999px;
    padding: 0.5rem 0.5rem 0.5rem 2rem;
    display: flex; align-items: center;
    box-shadow: 0 25px 50px -12px rgba(0,102,102,0.1);
    border: 1px solid rgba(0,102,102,0.1);
    max-width: 56rem; margin: 0 auto;
}
.floating-bar input {
    border: none; outline: none; flex-grow: 1;
    font-family: 'Inter', sans-serif; font-size: 1rem;
    color: #2c2f32; background: transparent; padding: 1rem 0;
}
.floating-bar input::placeholder { color: #000000; }

/* ── Sor button (inside form) ── */
.stFormSubmitButton > button {
    background: #006666 !important; color: #ffffff !important;
    border-radius: 9999px !important; font-family: 'Lexend', sans-serif !important;
    font-weight: 700 !important; font-size: 0.875rem !important;
    padding: 0.75rem 1.5rem !important; border: none !important;
    box-shadow: 0 10px 15px -3px rgba(0,102,102,0.2) !important;
    transition: all 0.2s ease !important; width: 100% !important;
    white-space: nowrap !important;
}
.stFormSubmitButton > button:hover {
    background: #005959 !important;
}
.stFormSubmitButton > button:active { transform: scale(0.95) !important; }

/* ── Sidebar buttons ── */
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important; color: #595c5f !important;
    border: none !important; border-radius: 0.5rem !important;
    padding: 0.75rem 1rem !important; box-shadow: none !important;
    font-family: 'Lexend', sans-serif !important; font-size: 0.75rem !important;
    font-weight: 700 !important; text-transform: uppercase !important;
    letter-spacing: 0.15em !important; text-align: left !important;
    transition: background 0.2s !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: #e5e8ed !important;
}

/* ── Text area (form) ── */
.stTextInput > div > div > input,
.stTextArea textarea {
    border: none !important; border-radius: 0 !important;
    padding: 1rem 0 !important; font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important; background: transparent !important;
    box-shadow: none !important; color: #000000 !important;
}
.stTextInput > div > div > input:focus,
.stTextArea textarea:focus { box-shadow: none !important; }
.stTextInput > div > div > input::placeholder,
.stTextArea textarea::placeholder { color: #000000 !important; }
.stTextInput > div > div {
    border-radius: 0 !important; border: none !important;
    background: transparent !important;
}
.stTextInput > div {
    border-radius: 0 !important; border: none !important;
    background: transparent !important;
}

/* ── Form wrapper → looks like floating bar ── */
[data-testid="stForm"] {
    background: #ffffff !important;
    border-radius: 9999px !important;
    padding: 0.25rem 0.5rem 0.25rem 2rem !important;
    box-shadow: 0 25px 50px -12px rgba(0,102,102,0.1) !important;
    border: 1px solid rgba(0,102,102,0.1) !important;
    max-width: 56rem !important; margin: 0 auto !important;
    display: flex !important; align-items: center !important;
    position: relative !important;
}
[data-testid="stForm"] > div {
    display: flex !important; align-items: center !important; flex-grow: 1; gap: 0;
    width: 100% !important;
}
[data-testid="stForm"] .stTextInput { flex-grow: 1; }
/* Remove gap between columns inside form */
[data-testid="stForm"] [data-testid="stHorizontalBlock"] {
    gap: 0 !important; align-items: center !important; width: 100% !important;
}
[data-testid="stForm"] [data-testid="stHorizontalBlock"] > div:first-child {
    flex-grow: 1 !important;
}
[data-testid="stForm"] [data-testid="stHorizontalBlock"] > div:last-child {
    flex-shrink: 0 !important; padding: 0 !important;
}

/* ── Question / answer boxes ── */
.q-box {
    background: #fff; color: #2c2f32; padding: 1.5rem;
    border-radius: 0.75rem; border: 1.5px solid rgba(0,102,102,0.15);
    margin: 0.75rem auto; white-space: pre-wrap; word-wrap: break-word;
    max-width: 56rem;
}
.q-box strong {
    color: #006666; font-family: 'Lexend', sans-serif; font-size: 0.75rem;
    font-weight: 700; display: block; margin-bottom: 0.5rem;
    text-transform: uppercase; letter-spacing: 0.1em;
}
.a-box {
    background: #fff; color: #2c2f32; padding: 2rem;
    border-radius: 0.75rem; border: 1.5px solid rgba(0,102,102,0.15);
    margin: 0.75rem auto; line-height: 1.8; min-height: 120px;
    white-space: pre-wrap; word-wrap: break-word;
    box-shadow: 0 4px 6px rgba(0,0,0,0.04);
    max-width: 56rem;
}
.a-box strong {
    color: #006666; font-family: 'Lexend', sans-serif; font-size: 0.75rem;
    font-weight: 700; display: block; margin-bottom: 1rem;
    text-transform: uppercase; letter-spacing: 0.1em;
}

/* ── Disclaimer ── */
.disclaimer {
    text-align: center; font-size: 0.625rem; color: #abadb1;
    text-transform: uppercase; letter-spacing: 0.15em;
    margin-top: 1rem; font-family: 'Inter', sans-serif;
}

/* ── Decorative blurs ── */
.blur-teal {
    position: fixed; top: 5rem; right: 5rem;
    width: 16rem; height: 16rem;
    background: rgba(0,102,102,0.05); border-radius: 9999px;
    filter: blur(60px); z-index: -1; pointer-events: none;
}
.blur-red {
    position: fixed; bottom: 10rem; left: 22rem;
    width: 24rem; height: 24rem;
    background: rgba(182,19,33,0.05); border-radius: 9999px;
    filter: blur(80px); z-index: -1; pointer-events: none;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }
.stDeployButton { display: none !important; }

/* ── Expander ── */
details summary span { font-family: 'Lexend', sans-serif !important; font-weight: 600 !important; }
details { background-color: #ffffff !important; border-radius: 0.75rem !important; border: 1px solid rgba(0,102,102,0.1) !important; }
details summary { background-color: #ffffff !important; color: #2c2f32 !important; }
details[open] > div { background-color: #ffffff !important; }

/* ── Spinner overlay ── */
div[data-testid="stSpinner"] { background-color: transparent !important; }
div[data-testid="stSpinner"] > div { background-color: transparent !important; }

/* ── Colored text & bg preservation ── */
.sb-brand-icon { background: #b61321 !important; color: #fff !important; }
.sb-brand-icon * { color: #fff !important; }
.sb-brand h2 { color: #b61321 !important; }
.sb-brand p { color: #595c5f !important; }
.sb-stats-value { color: #006666 !important; }
.sb-stats-title { color: #595c5f !important; }
.sb-stats-label { color: #595c5f !important; }
.sb-stats-status, .sb-stats-status * { color: #006666 !important; }
.sb-nav-item { color: #595c5f !important; }
.sb-nav-item.active { background: rgba(0,102,102,0.1) !important; color: #006666 !important; }
.sb-footer-item { color: #595c5f !important; }
.hero-title { color: #006666 !important; background: none !important; -webkit-text-fill-color: #006666 !important; }
.top-bar-logo { color: #006666 !important; background: none !important; -webkit-text-fill-color: #006666 !important; }
.top-nav a { color: #595c5f !important; }
.top-nav a.active { color: #006666 !important; }
.top-bar-right .material-symbols-outlined { color: #595c5f !important; }
.top-bar-avatar { background: #e5e8ed !important; }
.q-box strong, .a-box strong { color: #006666 !important; }
.hero-sub { color: #595c5f !important; }
.blur-teal { background: rgba(0,102,102,0.05) !important; }
.blur-red { background: rgba(182,19,33,0.05) !important; }
.disclaimer { color: #abadb1 !important; }

/* ── Sor button ── */
.stFormSubmitButton > button { background: #006666 !important; color: #ffffff !important; }
.stFormSubmitButton > button:hover { background: #005959 !important; color: #ffffff !important; }

/* ── Bento buttons text ── */
div[data-testid="column"] .stButton > button { color: #2c2f32 !important; }
</style>
""", unsafe_allow_html=True)

# ── Decorative blur circles ────────────────────────────────────────
st.markdown('<div class="blur-teal"></div><div class="blur-red"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# SIDEBAR  (matches HTML <aside> exactly)
# ══════════════════════════════════════════════════════════════════
with st.sidebar:
    api_key = os.getenv("OPENAI_API_KEY")
    api_status = "Online" if api_key else "Offline"

    st.markdown(f"""
    <div class="sb-brand">
        <div class="sb-brand-icon">
            <span class="material-symbols-outlined mso-fill" style="font-size:1.25rem">bolt</span>
        </div>
        <div>
            <h2>KINETIC ENGINE</h2>
            <p>API Status: {api_status}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Nav items (rendered as HTML; only Clear Data is interactive) ──
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:0.25rem;margin-bottom:1rem;">
        <div class="sb-nav-item active">
            <span class="material-symbols-outlined">speed</span> Dashboard
        </div>
        <div class="sb-nav-item">
            <span class="material-symbols-outlined">monitoring</span> Analytics
        </div>
        <div class="sb-nav-item">
            <span class="material-symbols-outlined">settings</span> System Config
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️  CLEAR DATA", use_container_width=True, key="clear"):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")

    # ── Session Stats ──
    q_count = len(st.session_state.chat_history)
    st.markdown(f"""
    <div class="sb-stats">
        <div class="sb-stats-title">Session Stats</div>
        <div class="sb-stats-grid">
            <div><div class="sb-stats-label">Duration</div><div class="sb-stats-value">--:--</div></div>
            <div><div class="sb-stats-label">Queries</div><div class="sb-stats-value">{q_count}</div></div>
        </div>
        <div class="sb-stats-status">
            <span class="material-symbols-outlined mso-fill" style="font-size:0.875rem">check_circle</span>
            SYSTEM CALIBRATED
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:0.25rem;">
        <div class="sb-footer-item"><span class="material-symbols-outlined" style="font-size:1rem">help</span> Support</div>
        <div class="sb-footer-item"><span class="material-symbols-outlined" style="font-size:1rem">logout</span> Log Out</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════════

# ── Top App Bar ────────────────────────────────────────────────────
st.markdown("""
<div class="top-bar">
    <div style="display:flex;align-items:center;gap:3rem">
        <span class="top-bar-logo">KINETIC AI</span>
        <div class="top-nav">
            <a href="#" class="active">Performance</a>
            <a href="#">History</a>
            <a href="#">Resources</a>
        </div>
    </div>
    <div class="top-bar-right">
        <span class="material-symbols-outlined">notifications</span>
        <span class="material-symbols-outlined">settings</span>
        <div class="top-bar-avatar"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-title">🏋️ RAG Personal Trainer</div>
<p class="hero-sub">Your AI-powered fitness assistant. Personalized knowledge, instantly.</p>
""", unsafe_allow_html=True)

# ── Bento Grid Quick Actions ──────────────────────────────────────
QUESTIONS = [
    ("fitness_center",   "How to do bench press?"),
    ("calendar_month",   "Suggest a 3-day strength program"),
    ("nutrition",        "Meal plan for weight gain"),
    ("timer",            "How long should a HIIT workout be?"),
    ("rebase_edit",      "Deadlift form correction tips"),
    ("local_fire_department", "Best fat-burning exercises"),
]

def ask(question: str):
    if st.session_state.trainer and st.session_state.loaded:
        with st.spinner("Generating response..."):
            answer = st.session_state.trainer.ask_question(question)
            st.session_state.chat_history.append({"question": question, "answer": answer})
            st.rerun()

# Row 1
c1, c2, c3 = st.columns(3)
for col, (icon, q) in zip([c1, c2, c3], QUESTIONS[:3]):
    with col:
        if st.button(f"🔹 {q}", key=f"bento_{q[:10]}"):
            ask(q)

# Row 2
c4, c5, c6 = st.columns(3)
for col, (icon, q) in zip([c4, c5, c6], QUESTIONS[3:]):
    with col:
        if st.button(f"🔹 {q}", key=f"bento_{q[:10]}"):
            ask(q)

# ── Floating Input Bar ────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

with st.form("ask_form", clear_on_submit=True):
    col_input, col_btn = st.columns([10, 1])
    with col_input:
        user_q = st.text_input("Question", placeholder="Type your question...", label_visibility="collapsed")
    with col_btn:
        submitted = st.form_submit_button("➤")

if submitted and user_q.strip():
    ask(user_q.strip())

st.markdown('<p class="disclaimer">Kinetic AI can make mistakes. Check important information.</p>', unsafe_allow_html=True)

# ── Answer display (latest at top) ────────────────────────────────
if st.session_state.chat_history:
    latest = st.session_state.chat_history[-1]
    safe_q = html_module.escape(latest["question"])
    safe_a = html_module.escape(latest["answer"])
    st.markdown(f'<div class="q-box"><strong>Question</strong>{safe_q}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="a-box"><strong>AI Response</strong>{safe_a}</div>', unsafe_allow_html=True)

    if len(st.session_state.chat_history) > 1:
        st.markdown("---")
        for chat in reversed(st.session_state.chat_history[:-1]):
            sq = html_module.escape(chat["question"])
            sa = html_module.escape(chat["answer"])
            with st.expander(f"💬 {chat['question'][:60]}…"):
                st.markdown(f'<div class="q-box"><strong>Question</strong>{sq}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="a-box"><strong>AI Response</strong>{sa}</div>', unsafe_allow_html=True)
