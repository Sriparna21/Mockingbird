from database.auth import verify_user
from utils.styling import apply_background
import streamlit as st

apply_background('utils/background.jpg')

st.set_page_config(layout='centered')

# left,center,right = st.columns([2,5,2])

st.title('MockingBird')
st.markdown("<br><br>", unsafe_allow_html=True)

snm = st.text_input('Enter your username')
pswd = st.text_input('Enter your password',type='password')

col1,col2 = st.columns(2)

with col1:

    if st.button('Login',use_container_width=True):
     res = verify_user(usnm,pswd)

     if res:
        st.success('User logged in successfully!')
        st.switch_page('pages/1_profile.py')
     else:
        st.error('Login failed!')


with col2:

    if st.button('Singup',use_container_width=True):
        st.switch_page('pages/3_register.py')



