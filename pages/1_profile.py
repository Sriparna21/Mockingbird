from utils.styling import apply_background
from database.auth import logout
import streamlit as st

apply_background('utils/background.jpg')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page('pages/app.py')

if st.session_state.logged_in:

    

    st.write('So this works real time?')
    store = st.text_input('Taking my input here like I know something!')

    st.write('Saying',store)
    st.button('Click me to save your life')

    with st.sidebar: 
        if st.button('Logout'):
            logout()