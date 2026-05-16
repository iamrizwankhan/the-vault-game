import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="The Vault",
    page_icon="🔐",
    layout="centered"
)

# ---------------- GAME LOGIC ----------------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 50)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ---------------- STYLING ----------------
st.markdown("""
<style>

.stApp {
    background-color: #edf2f4;
    color: #0b245b;
}

.main-title {
    text-align: center;
    font-size: 64px;
    font-weight: 800;
    color: #0b245b;
    margin-top: 20px;
}

.sub-text {
    text-align: center;
    font-size: 24px;
    color: #4f6485;
    margin-bottom: 40px;
}

.block-container {
    padding-top: 2rem;
    max-width: 750px;
}

.card {
    background-color: white;
    padding: 35px;
    border-radius: 24px;
    margin-top: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

.history-card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

.big-text {
    font-size: 32px;
    font-weight: 700;
    color: #0b245b;
    text-align: center;
}

label {
    color: #0b245b !important;
    font-weight: 600 !important;
    font-size: 18px !important;
}

.stButton > button {
    width: 100%;
    background-color: #0b245b;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px;
    font-size: 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #163b8c;
    color: white;
}

.stNumberInput input {
    background-color: #f8fafc !important;
    color: #0b245b !important;
    border-radius: 12px !important;
    font-size: 28px !important;
    text-align: center !important;
    border: 2px solid #dbe4ea !important;
}

div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<div class='main-title'>🔐 The Vault</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-text'>Crack the combination.</div>",
    unsafe_allow_html=True
)

# ---------------- DIFFICULTY ----------------
difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

if difficulty == "Easy":
    max_attempts = 10
elif difficulty == "Medium":
    max_attempts = 5
else:
    max_attempts = 3

# ---------------- MAIN CARD ----------------


guess = st.number_input(
    "Guess a number between 1 and 50",
    min_value=1,
    max_value=50,
    step=1
)

# ---------------- SUBMIT ----------------
if st.button("Submit Guess"):

    if not st.session_state.game_over:

        st.session_state.attempts += 1
        attempts_left = max_attempts - st.session_state.attempts

        if guess == st.session_state.number:

            st.markdown(f"""
<div style="
background:#dcfce7;
padding:22px;
border-radius:14px;
margin-top:20px;
font-size:24px;
font-weight:700;
color:#166534;
text-align:center;
">
🎉 Vault Opened!<br>
You cracked the code in {st.session_state.attempts} attempts.
</div>
""", unsafe_allow_html=True)

            st.session_state.game_over = True

        elif guess < st.session_state.number:

           st.markdown(f"""
<div style="
background:#fee2e2;
padding:18px;
border-radius:12px;
margin-top:20px;
font-size:22px;
font-weight:700;
color:#7f1d1d;
">
📉 Too Low! Attempts Left: {attempts_left}
</div>
""", unsafe_allow_html=True)

        else:

            st.markdown(f"""
<div style="
background:#dbeafe;
padding:18px;
border-radius:12px;
margin-top:20px;
font-size:22px;
font-weight:700;
color:#1e3a8a;
">
📈 Too High! Attempts Left: {attempts_left}
</div>
""", unsafe_allow_html=True)

        st.session_state.history.append(guess)

        if attempts_left == 0 and guess != st.session_state.number:

            st.markdown(f"""
<div style="
background:#fecaca;
padding:22px;
border-radius:14px;
margin-top:20px;
font-size:24px;
font-weight:700;
color:#991b1b;
text-align:center;
">
💥 Game Over!<br>
The correct number was {st.session_state.number}
</div>
""", unsafe_allow_html=True)

            st.session_state.game_over = True

# ---------------- PLAY AGAIN ----------------
if st.button("Play Again"):

    st.session_state.number = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_over = False

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HISTORY ----------------
st.markdown("<div class='history-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='big-text'>Guess History</div>",
    unsafe_allow_html=True
)

if st.session_state.history:

    for item in reversed(st.session_state.history):
        st.write(f"🔹 {item}")

else:
    st.write("No guesses yet.")

st.markdown("</div>", unsafe_allow_html=True)
