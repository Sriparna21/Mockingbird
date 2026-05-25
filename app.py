from database.auth import login_check
from utils.styling import apply_background
import streamlit as st

apply_background('utils/background.jpg')

st.set_page_config(layout='centered')

# left,center,right = st.columns([2,5,2])

if "logged_in" not in st.session_state:
   st.session_state.logged_in = False

if st.session_state.logged_in:
   st.switch_page('pages/1_profile.py')


st.title('MockingBird')
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


usnm = st.text_input('Enter your username')
pswd = st.text_input('Enter your password',type='password')

col1,col2 = st.columns(2)

with col1:

    if st.button('Login',use_container_width=True):
     res = login_check(usnm,pswd)

     if res:
        st.success('User logged in successfully!')
        st.switch_page('pages/1_profile.py')
     else:
        st.error('Login failed!')


with col2:

    if st.button('Singup',use_container_width=True):
        st.switch_page('pages/3_register.py')





