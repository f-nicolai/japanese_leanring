import streamlit as st
from utils.wrapers import read_markdown_file
from pathlib import Path

def render_page(resource:str):
    st.title(f"Lessons")
    if st.button("Back to Main Menu",key='lessons_back_1'):
        st.session_state.page = 'main'
        st.rerun()
    st.write('\n')

    if resource == 'te_form':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/forme en -te.md'),unsafe_allow_html=True)
    elif resource == 'past_polite':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/forme polie au passé.md'),unsafe_allow_html=True)
    elif resource == 'adj_negation':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/negations_adjectifs.md'),unsafe_allow_html=True)
    elif resource == 'invitation':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/expressing_desire_and_invitation.md'),unsafe_allow_html=True)
    elif resource == 'concat_verbs':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/connecter des verbes.md'),unsafe_allow_html=True)
    elif resource == 'concat_adj':
        st.markdown(read_markdown_file(Path(__file__).parent.parent/'lessons/connecter des adjectifs.md'),unsafe_allow_html=True)

    st.write('\n')
    if st.button("Back to Main Menu",key='lessons_back_2'):
        st.session_state.page = 'main'
        st.rerun()

