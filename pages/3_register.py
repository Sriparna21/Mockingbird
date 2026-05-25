import streamlit as st
from database.crud import add_users
from utils.styling import apply_background
from utils.logger import logger


apply_background('utils/background.jpg')

st.set_page_config(layout='centered')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


left,center,right = st.columns([2,5,2])


with center:
    st.title('Registration')

    st.markdown("<br><br>", unsafe_allow_html=True)

    nm = st.text_input('Enter your name here')
    usnm = st.text_input('Enter your username')
    pswd = st.text_input('Enter your password',type='password')
    confirm_pswd = st.text_input('Enter your password')

    if st.button('Register'):
        if  nm and  usnm and pswd and confirm_pswd:
    

            if pswd == confirm_pswd:
                res = add_users(nm,usnm,pswd)

                if res['success']:
                    logger.info(f'User {nm} successfully registered')
                    st.success(res['message'])
                    st.switch_page('app.py')
                else:
                    logger.warning(f'Failed registration for user {nm}')
                    st.error(res['message'])
            else:
                st.error("Error, passwords don't match. Please try again")
        else:
            logger.warning(f'Registration attempted with an empty field')
            st.error(f'All fields are required for registration')