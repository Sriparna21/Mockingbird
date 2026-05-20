from utils.styling import apply_background
import streamlit as st

apply_background('utils/background.jpg')

st.write('So this works real time?')
store = st.text_input('Taking my input here like I know something!')

st.write('Saying',store)
st.button('Click me to save your life')