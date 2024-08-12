import streamlit as st
from .config_tab import get_dataframe_filter, initialize_without_replacement_dataframe
from pandas import DataFrame
from utils.styling import st_write_centered
from utils.wrapers import create_back_and_next_buttons


def render_page():
    st.title("Verbs quizz")

    create_back_and_next_buttons()
    create_verbs_quizz_direction_radio_buttons()

    sample = get_sample(current_state=st.session_state['kanji_quizz.current_state'])

    if st.session_state['kanji_quizz.current_state'] == 'original':
        st_write_centered(
            sample[st.session_state.verbs_direction[st.session_state['verbs.from']]].squeeze(),
            font_size=100 if st.session_state['verbs.from'] in ('English','French','Romanji') else 200
        )

    elif st.session_state['kanji_quizz.current_state'] == 'translation':
        st_write_centered(
            f"{sample[st.session_state.verbs_direction[st.session_state['verbs.to']]].squeeze()}",
            font_size=200,
        )
        if st.session_state['verbs.to'] == 'Polite':
            st_write_centered(
                f"{sample['hiragana'].squeeze()}",
                font_size=100,
                style_name='medium-font'
            )
            st_write_centered(
                f"{sample['romanji'].squeeze()}",
                font_size=100,
                style_name='medium-font'
            )

def get_sample(current_state: str) -> DataFrame:
    if current_state == 'original':
        if st.session_state['config.random']:
            sample = st.session_state.verbs_sample_without_replacement.sample(1)
            st.session_state.verbs_sample_without_replacement = st.session_state.verbs_sample_without_replacement.drop(
                sample.index)
            if st.session_state.verbs_sample_without_replacement.shape[0] == 0:
                st.session_state.verbs_sample_without_replacement = initialize_without_replacement_dataframe(
                    resource='verbs')

        else:
            filter = get_dataframe_filter(resource='verbs')
            sample = st.session_state.verbs \
                .loc[filter] \
                .sample(1)

        st.session_state.sample = sample

    return st.session_state.sample


def create_verbs_quizz_direction_radio_buttons():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.selectbox("Guess from :", st.session_state.verbs_direction.keys(), key='verbs.from')
    with col4:
        st.selectbox("To :", st.session_state.verbs_direction.keys(), key='verbs.to')
