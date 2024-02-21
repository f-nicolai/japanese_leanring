import streamlit as st

def render_config_tab():
    with st.sidebar:
        st.header("Configuration")
        st.checkbox("Checkbox 1", key="checkbox1")
        st.checkbox("Checkbox 2", key="checkbox2")
        st.checkbox("Checkbox 3", key="checkbox3")
        st.radio("Radio Option", ["Option 1", "Option 2"], key="radio_option")
        st.selectbox("Dropdown List", ["Option A", "Option B"], key="dropdown_option")
