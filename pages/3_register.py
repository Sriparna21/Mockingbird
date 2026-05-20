import streamlit as st
from database.crud import add_users
from utils.styling import apply_background


apply_background('utils/background.jpg')

st.set_page_config(layout='centered')

left,center,right = st.columns([2,5,2])

with center:
    st.title('Registration')

    st.markdown("<br><br>", unsafe_allow_html=True)

    nm = st.text_input('Enter your name here')
    usnm = st.text_input('Enter your username')
    pswd = st.text_input('Enter your password',type='password')
    confirm_pswd = st.text_input('Enter your password')

    if st.button('Register'):

        if pswd == confirm_pswd:
            res = add_users(nm,usnm,pswd)

            if res['success']:
                st.success(res['message'])
                st.switch_page('pages/1_profile.py')
            else:
                st.error(res['message'])
        else:
            st.error("Error, passwords don't match. Please try again")