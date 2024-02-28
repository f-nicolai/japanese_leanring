import streamlit as st
from .config_tab import get_dataframe_filter, initialize_without_replacement_dataframe
from pandas import DataFrame
from utils.styling import st_write_centered
from utils.wrapers import create_back_and_next_buttons


def render_page():
    st.title("Guess the Kanji !")

    create_back_and_next_buttons()

    sample = get_sample(current_state=st.session_state['kanji_quizz.current_state'])

    if st.session_state['kanji_quizz.current_state'] == 'original':
        st_write_centered(sample['kanji'].squeeze(), font_size=200)


    elif st.session_state['kanji_quizz.current_state'] == 'translation':
        st_write_centered(f":red[{sample['romanji'].squeeze()}]", font_size=100,style_name='red-label')
        display = sample[st.session_state['config.language'].lower()].squeeze().replace(',', ' / ')
        st_write_centered(display,font_size=100)


def get_sample(current_state: str) -> DataFrame:
    if current_state =='original':
        if st.session_state['config.random']:
            sample = st.session_state.kanji_sample_without_replacement.sample(1)
            st.session_state.kanji_sample_without_replacement = st.session_state.kanji_sample_without_replacement.drop(sample.index)
            if st.session_state.kanji_sample_without_replacement.shape[0] == 0:
                st.session_state.kanji_sample_without_replacement = initialize_without_replacement_dataframe(resource='words')

        else :
            filter = get_dataframe_filter(resource='words')
            sample = st.session_state.kanjis \
                .loc[lambda x: (~x['kanji'].isnull()) & filter] \
                .sample(1)

        st.session_state.sample = sample

    return st.session_state.sample