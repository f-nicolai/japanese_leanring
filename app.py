import streamlit as st
from pages import config_tab, lessons, translate_from_japanese, translate_to_japanese, resources, review_verbs, \
    main_page

st.set_page_config(layout="wide")

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'
    config_tab.initialize_internal_config()

config_tab.render_config_tab()

# Page routing
if st.session_state['page'] == 'main':
    main_page.render_main_page()
elif st.session_state['page'] == 'to_japanese':
    translate_to_japanese.render_page()
elif st.session_state['page'] == 'from_japanese':
    translate_from_japanese.render_page()
elif st.session_state['page'] == 'review_verbs':
    review_verbs.render_page()
elif st.session_state['page'] in ('show_words', 'show_verbs', 'show_counters'):
    resources.render_page(resource=st.session_state['page'])
elif st.session_state['page'] in ('te_form', 'past_polite', 'adj_negation', 'invitation', 'concat_verbs', 'concat_adj'):
    lessons.render_page(resource=st.session_state['page'])
