import streamlit as st
from utils.styling import apply_background
from report_service.campaign_overview import (get_campaign_overview)
import plotly.express as px
from database.auth import logout

st.set_page_config(layout="wide")
apply_background('utils/background.jpg')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page('app.py')
    st.stop()

if "campaign_overview" not in st.session_state.reports_to_view:
    logger.warning(f'User {st.session_state} does not have access to view the report - Campaign Overview')

st.title('Campaign Overview')
st.markdown("<br>", unsafe_allow_html=True)


st.write('This is a summary report containing information regarding the performance of all the campaigns.')

st.markdown("<br><br>", unsafe_allow_html=True)

k1,k2,k3,k4 = st.columns(4)

report_df = get_campaign_overview()
report_df_metrics = report_df[report_df['outcome'] != 'NA']
# st.dataframe(report_df)

k1.metric("Total Campaigns",report_df.campaign.nunique())
k2.metric('Success Rate',
          f"{round(((report_df_metrics[report_df_metrics['outcome'] == 'success']['outcome_count'].sum()/report_df_metrics['outcome_count'].sum())*100),2)}%")
k3.metric('Failure Rate',
          f"{round(((report_df_metrics[report_df_metrics['outcome'] == 'failure']['outcome_count'].sum()/report_df_metrics['outcome_count'].sum())*100),2)}%")
k4.metric('Data Coverage percentage',f"{round(((report_df_metrics['outcome_count'].sum()/report_df['outcome_count'].sum())*100),2)}%")

st.markdown("<br><br>", unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    outcome_mapping = {
        'All': 'All',
        'Success': 'success',
        'Failure': 'failure',
        'NA': 'NA'
    }

    selected_display = st.selectbox('Select Outcome',outcome_mapping.keys())

    selected_outcome = outcome_mapping[selected_display]

    if selected_outcome != 'All':
        filtered_df = report_df[report_df['outcome'] == selected_outcome]
    else:
        filtered_df = report_df
    


with col2:
    selected_count = st.selectbox('Select count',[5,10,15,20,'All'])

    if selected_count != 'All':

        # Logic for ALL outcomes
        if selected_outcome == 'All':

            top_campaigns = (
                filtered_df
                .groupby('campaign')['outcome_count']
                .sum()
                .sort_values(ascending=False)
                .head(selected_count)
                .index
            )

            filtered_count = filtered_df[
                filtered_df['campaign'].isin(top_campaigns)
            ]

        # Logic for single outcome
        else:

            filtered_count = (
                filtered_df
                .sort_values(
                    by='outcome_count',
                    ascending=False
                )
                .head(selected_count)
            )

    else:
        filtered_count = filtered_df
    

st.markdown("<br><br>", unsafe_allow_html=True)    


bar_chart_data = filtered_count.pivot(
        index = 'campaign',
        values = 'outcome_count',
        columns = 'outcome'
    )

st.bar_chart(bar_chart_data)

with st.expander("View Raw Data"):

    st.dataframe(bar_chart_data)

if "campaign_overview" in st.session_state.reports_to_download:
    logger.info(f'User {st.session_state.username} is downloading the report - Campaign overview')
    st.download_button(
        label = 'Download Report',
        data = bar_chart_data.to_csv(index=False),
        file_name='Campaign_overview.csv',
        mime='text/csv'
    )

with st.sidebar: 
        if st.button('Logout'):
            logger.info(f'User {st.session_state.username} logged out')
            logout()       
