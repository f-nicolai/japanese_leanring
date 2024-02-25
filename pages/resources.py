import streamlit as st
from random import randint


def render_page(resource:str):
    st.title(f"Resources - {resource.replace('show_','').upper()}")
    if st.button("Back to Main Menu",key='resources_back_1'):
        st.session_state.page = 'main'
        st.rerun()
    st.write('\n')

    if resource == 'show_verbs':
        # st.dataframe(st.session_state.verbs.drop(['section','unit'],axis=1).style.hide(axis="index"),use_container_width=True)
        st.markdown(st.session_state.verbs.drop(['section','unit'],axis=1).style.hide(axis="index").to_html(),unsafe_allow_html=True)
    elif resource == 'show_words':
        # st.dataframe(st.session_state.kanjis.drop(['section','unit'],axis=1).style.hide(axis="index"),use_container_width=True)
        st.markdown(st.session_state.kanjis.drop(['section','unit'],axis=1).style.hide(axis="index").to_html(),unsafe_allow_html=True)

    elif resource == 'show_counters':
        # st.dataframe(st.session_state.counters.drop(['section','unit'],axis=1).style.hide(axis="index"),use_container_width=True)
        st.markdown(st.session_state.counters.drop(['section','unit'],axis=1).style.hide(axis="index").to_html(),unsafe_allow_html=True)

    st.write('\n')
    if st.button("Back to Main Menu",key='resources_back_2'):
        st.session_state.page = 'main'
        st.rerun()

