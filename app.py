import streamlit as st

# App Title
st.set_page_config(page_title="ShortsCoin", page_icon="💰")

st.title("💰 ShortsCoin")
st.subheader("Create • Earn • Grow 🚀")

# Initialize coins
if "coins" not in st.session_state:
    st.session_state.coins = 0

# Buttons
if st.button("🎬 Watch Short (Earn 5 Coins)"):
    st.session_state.coins += 5
    st.success("You earned 5 coins 🎉")

if st.button("📢 Share App (Earn 10 Coins)"):
    st.session_state.coins += 10
    st.success("You earned 10 coins 🚀")

# Display coins
st.write(f"### 🪙 Total Coins: {st.session_state.coins}")

# Simple leaderboard (demo)
st.write("## 🏆 Leaderboard")
st.write("1. User123 - 150 coins")
st.write("2. You - Keep earning 💪")
