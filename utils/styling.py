import streamlit as st
import base64


def get_base64(file):

    with open(file, "rb") as f:
        data = f.read()

    return base64.b64encode(data).decode()


def apply_background(image_file):

    bg_image = get_base64(image_file)

    st.markdown(
        f"""
        <style>

        .stApp {{

            background-image: url(
                "data:image/jpg;base64,{bg_image}"
            );

            background-size: cover;

            background-position: center;

            background-repeat: no-repeat;

            background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )