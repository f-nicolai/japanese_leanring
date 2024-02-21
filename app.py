import streamlit as st

# Assuming other page modules are defined similarly to previous examples
from pages import config_tab, english_to_kanji, kanji_to_english

def render_main_page():
    st.title("Quiz App")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start English to Kanji Quiz"):
            st.session_state['page'] = 'english_to_kanji'
            st.rerun()
    with col2:
        if st.button("Start Kanji to English Quiz"):
            st.session_state['page'] = 'kanji_to_english'
            st.rerun()

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

config_tab.render_config_tab()  # Assuming this function renders the config sidebar

# Page routing
if st.session_state['page'] == 'main':
    render_main_page()
elif st.session_state['page'] == 'english_to_kanji':
    english_to_kanji.render_page()
elif st.session_state['page'] == 'kanji_to_english':
    kanji_to_english.render_page()
