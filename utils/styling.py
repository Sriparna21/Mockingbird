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

        /* Transparent top header */

        [data-testid="stHeader"] {{

            background: rgba(0,0,0,0);
        }}

        /* Sidebar styling */

        [data-testid="stSidebar"] {{

            background-color: rgba(20,20,30,0.95);
        }}

        /* Hide report pages from sidebar */

        [data-testid="stSidebarNav"] ul li:nth-child(1),
        [data-testid="stSidebarNav"] ul li:nth-child(4),
        [data-testid="stSidebarNav"] ul li:nth-child(5),
        [data-testid="stSidebarNav"] ul li:nth-child(6),
        [data-testid="stSidebarNav"] ul li:nth-child(7),
        [data-testid="stSidebarNav"] ul li:nth-child(8) {{

            display: none;
        }}

        /* KPI metric cards */

        div[data-testid="stMetric"] {{

            background-color: rgba(0,0,0,0.20);

            padding: 15px;

            border-radius: 12px;

            border: 1px solid rgba(255,255,255,0.08);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

