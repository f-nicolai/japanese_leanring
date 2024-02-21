import streamlit as st
from random import randint


def render_page():
    st.title("Kanji to English Quiz")

    if "random_string" not in st.session_state:
        st.session_state.random_string = "KANJI TO ENGLISH"

    st.write(st.session_state.random_string)

    if st.button("Next") or st.session_state.get("enter_pressed", False):
        # Update random_string with a new value
        st.session_state.random_string = f'{randint(0,100)}'  # Update this with actual logic
        st.session_state.enter_pressed = False

    if st.button("Back"):
        st.session_state.current_page = "main"
