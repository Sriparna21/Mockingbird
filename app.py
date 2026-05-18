from database.auth import verify_user
import streamlit as st

st.set_page_config(layout='centered')

left,center,right = st.columns([2,5,2])
    

with center:
    st.title('MockingBird')

    st.markdown("<br><br>", unsafe_allow_html=True)

    usnm = st.text_input('Enter your username')
    pswd = st.text_input('Enter your password',type='password')

    if st.button('Login'):
        res = verify_user(usnm,pswd)

        if res:
            st.success('User logged in successfully!')
            st.switch_page('pages/1_profile.py')
        else:
            st.error('Login failed!')



