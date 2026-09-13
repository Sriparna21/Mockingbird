import streamlit as st
from utils.styling import apply_background
from report_service.campaign_effectiveness import (get_campaign_effectiveness)
import plotly.express as px
from database.auth import logout
import logging
import requests
import pandas as pd


st.set_page_config(layout="wide")
apply_background('utils/background.jpg')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page('app.py')
    st.stop()

logging.basicConfig(level=logging.info)
logger = logging.getLogger(__name__)


if "campaign_effectiveness" not in st.session_state.reports_to_view:
    logger.warning(f'User {st.session_state} does not have access to view the report - Campaign Effectiveness')

st.title('Campaign Effectiveness Report')
st.markdown("<br>", unsafe_allow_html=True)


st.write('This is a summary report detailing campaign performance.')

# st.markdown("<br>", unsafe_allow_html=True)

response = requests.get('http://127.0.0.1:8000/campaign/effectiveness')
data = response.json()

report_df = pd.DataFrame(data)
metrics_df = report_df[report_df.outcome != 'NA']
# st.dataframe(metrics_df)

pivot_df = metrics_df.pivot(index='campaign',columns ='outcome',values = 'outcome_count')
pivot_df = pivot_df.fillna(0)
pivot_df['Total'] = pivot_df['success'] + pivot_df['failure']
pivot_df['Success%'] = round((pivot_df['success']/pivot_df['Total'])*100,2)
pivot_df['Failure%'] = round((pivot_df['failure']/pivot_df['Total'])*100,2)
#st.dataframe(pivot_df)

k1,k2,k3,k4= st.columns(4)

top_campaigns = (
    pivot_df.sort_values(by='Success%',ascending = False).head(5).index.astype(str).tolist()
)
bottom_campaigns = (
    pivot_df.sort_values(by='Failure%',ascending = False).head(5).index.astype(str).tolist()
)

k1.metric('Best performing campaigns',', '.join(top_campaigns))
k2.metric('Worst performing campaigns',', '.join(bottom_campaigns))
k3.metric('Best conversion rate', f"{pivot_df.sort_values(by='Success%',ascending = False)['Success%'].iloc[0]}%")
k4.metric('Worst conversion rate', f"{pivot_df.sort_values(by='Failure%',ascending = False)['Failure%'].iloc[0]}%")

st.divider()

col1, col2 = st.columns(2)



with col1:

    with st.container(border=True):
        h1, h2 = st.columns([5,2])

        with h2:

            outcome_selector = st.radio(
                '',
                ['Success','Failure'],
                horizontal=True,
                label_visibility='collapsed'
            )

        with h1:

            st.subheader(
                f'{outcome_selector} Rate by Campaign'
            )

        

        fig = px.bar(
            pivot_df.reset_index(),
            x = f'{outcome_selector}%',
            y = 'campaign',
            orientation = 'h',
            text = f'{outcome_selector}%',
            color  = f'{outcome_selector}%',
            color_continuous_scale='Oranges'
        )

        fig.update_layout(
            height=510,
            margin=dict(t=20, b=20),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True,config={'displayModeBar': False})


with col2:
    with st.container(border=True):
        lb = (pivot_df.sort_values(by='Success%',ascending = False).reset_index())
        lb['Rank'] = range(1,len(lb)+1)
        st.subheader('Performance Leaderboard 🏆')

        st.dataframe(
            lb,
            use_container_width=True,
            height=460
        )
        if "campaign_effectiveness" in st.session_state.reports_to_download:
            logger.info(f'User {st.session_state.username} is downloading the report - Campaign Effectiveness')
            st.download_button(
                label = 'Download Report',
                data = lb.to_csv(index=True),
                file_name='Campaign_effectiveness.csv',
                mime='text/csv'
                )


with st.sidebar: 
        if st.button('Logout'):
            logger.info(f'User {st.session_state.username} logged out')
            logout()       

