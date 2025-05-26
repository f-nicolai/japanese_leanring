import streamlit as st
from .config_tab import initialize_without_replacement_dataframe

def render_main_page():
    st.title('Japanese Learning Quizz')

    st.header('Quizz:')
    st.write('\n')

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Translate from Japanese',use_container_width=True):
            st.session_state['page'] = 'from_japanese'
            st.session_state.kanji_sample_without_replacement = initialize_without_replacement_dataframe(resource='words')
            st.rerun()
    with col2:
        if st.button('Translate to Japanese',use_container_width=True):
            st.session_state['page'] = 'to_japanese'
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
    with col6:
        if st.button('Négation des adjectifs', use_container_width=True):
            st.session_state['page'] = 'adj_negation'
            st.rerun()

    col7, col8, col9 = st.columns(3)
    with col7:
        if st.button("Exprimer désir & invitation", use_container_width=True):
            st.session_state['page'] = 'invitation'
            st.rerun()
    with col8:
        if st.button("Concaténer des verbes", use_container_width=True):
            st.session_state['page'] = 'concat_verbs'
            st.rerun()
    with col9:
        if st.button("Concaténer des adjectifs", use_container_width=True):
            st.session_state['page'] = 'concat_adj'
            st.rerun()

    col10, col11, col12 = st.columns(3)
    with col10:
        if st.button("Forme のだ et なの", use_container_width=True):
            st.session_state['page'] = 'nano_noda'
            st.rerun()
    with col11:
        if st.button("Mettre au conditionnel", use_container_width=True):
            st.session_state['page'] = 'cond_capacity'
            st.rerun()
    with col12:
        if st.button("Action faite pour quelqu’un", use_container_width=True):
            st.session_state['page'] = 'from_to'
            st.rerun()

    col13, col14, col15 = st.columns(3)
    with col13:
        if st.button("Cheat sheet", use_container_width=True):
            st.session_state['page'] = 'cheat_sheet'
            st.rerun()

    st.write('\n')
    st.header('Resources:')
    col16, col17, col18 = st.columns(3)

    with col16:
        if st.button('Words list',use_container_width=True):
            st.session_state['page'] = 'show_words'
            st.rerun()
    with col17:
        if st.button('Verbs',use_container_width=True):
            st.session_state['page'] = 'show_verbs'
            st.rerun()
    with col18:
        if st.button('All counters',use_container_width=True):
            st.session_state['page'] = 'show_counters'
            st.rerun()