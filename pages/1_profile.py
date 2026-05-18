import streamlit as st

st.write('So this works real time?')
store = st.text_input('Taking my input here like I know something!')

st.write('Saying',store)
st.button('Click me to save your life')