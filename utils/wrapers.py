import streamlit as st
from pathlib import Path

def create_back_and_next_buttons():

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Main Menu"):
            st.session_state.page = 'main'
            st.session_state['kanji_quizz.current_state'] = 'original'
            st.rerun()

    with col2:
        if st.button("Next", use_container_width=True):
            if st.session_state['kanji_quizz.current_state'] == 'translation':
                st.session_state['kanji_quizz.current_state'] = 'original'
            elif st.session_state['kanji_quizz.current_state'] == 'original':
                st.session_state['kanji_quizz.current_state'] = 'translation'

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()