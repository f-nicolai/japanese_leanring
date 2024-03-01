import streamlit as st
from .config_tab import initialize_without_replacement_dataframe

def render_main_page():
    st.title('Japanese Learning Quizz')

    st.header('Quizz:')
    st.write('\n')

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Guess the Kanji',use_container_width=True):
            st.session_state['page'] = 'guess_kanji'
            st.session_state.kanji_sample_without_replacement = initialize_without_replacement_dataframe(resource='words')
            st.rerun()
    with col2:
        if st.button('Translate to Kanji',use_container_width=True):
            st.session_state['page'] = 'translate_kanji'
            st.session_state.kanji_sample_without_replacement = initialize_without_replacement_dataframe(resource='words')
            st.rerun()
    with col3:
        if st.button('Review your verbs',use_container_width=True):
            st.session_state['page'] = 'review_verbs'
            st.session_state.verbs_sample_without_replacement = initialize_without_replacement_dataframe(resource='verbs')
            st.rerun()

    st.write('\n')
    st.header('Lessons [FR]:')
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("'Forme -te: Actions en cours / Impératif / Suite d'action", use_container_width=True):
            st.session_state['page'] = 'te_form'
            st.rerun()
    with col5:
        if st.button('Forme polie au passé', use_container_width=True):
            st.session_state['page'] = 'past_polite'
            st.rerun()


    st.write('\n')
    st.header('Resources:')
    col7, col8, col9 = st.columns(3)

    with col7:
        if st.button('Words list',use_container_width=True):
            st.session_state['page'] = 'show_words'
            st.rerun()
    with col8:
        if st.button('Verbs',use_container_width=True):
            st.session_state['page'] = 'show_verbs'
            st.rerun()
    with col9:
        if st.button('All counters',use_container_width=True):
            st.session_state['page'] = 'show_counters'
            st.rerun()