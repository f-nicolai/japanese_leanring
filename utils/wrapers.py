import streamlit as st
from pathlib import Path

from pandas import concat


def create_back_and_next_buttons(add_focus_word_button: bool = False):
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

    if add_focus_word_button:
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Add to focus group", use_container_width=True):
                st.session_state.focus_words = concat([
                    st.session_state.focus_words.loc[
                        lambda x: x['kanji'] != st.session_state.sample['kanji'].iloc[0]
                    ],
                    st.session_state.sample
                ])
                st.session_state.just_modified_to_focus_group = True

        with col4:
            if st.button("Remove from focus group", use_container_width=True):
                st.session_state.focus_words = st.session_state.focus_words.loc[
                    lambda x: x['kanji'] != st.session_state.sample['kanji'].iloc[0]
                ]
                st.session_state.just_modified_to_focus_group = True


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding='utf-8')
