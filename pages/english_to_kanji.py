import streamlit as st
import random

def render_page():
    st.title("English to Kanji Quiz")
    # Display random string logic here
    if 'random_string' not in st.session_state:
        st.session_state['random_string'] = 'Initial String'
    st.write(st.session_state['random_string'])

    if st.button("Next"):
        # Update the random string
        st.session_state['random_string'] = get_random_string()
        st.rerun()  # Force rerun to refresh the page and show the new string

    if st.button("Back to Main Menu"):
        st.session_state.page = 'main'
        st.rerun()

def get_random_string():
    # Return a new random string
    example_strings = ["String 1", "String 2", "String 3", "String 4"]
    return random.choice(example_strings)
