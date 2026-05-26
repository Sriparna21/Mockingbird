import streamlit as st
from report_service.campaign_overview import (get_campaign_overview)
import plotly.express as px

st.title('Campaign Overview')
st.markdown("<br>", unsafe_allow_html=True)

st.write('This is a summary report containing information regarding the performance of all the campaigns.')

st.markdown("<br>", unsafe_allow_html=True)

k1,k2,k3,k4 = st.columns(4)

report_df = get_campaign_overview()
report_df_metrics = report_df[report_df['outcome'] != 'NA']
# st.dataframe(report_df)

k1.metric("Total Campaigns",report_df.campaign.nunique())
k2.metric('Success Rate',
          f"{round(((report_df_metrics[report_df_metrics['outcome'] == 'success']['outcome_count'].sum()/report_df_metrics['outcome_count'].sum())*100),2)}%")
k3.metric('Failure Rate',
          f"{round(((report_df_metrics[report_df_metrics['outcome'] == 'failure']['outcome_count'].sum()/report_df_metrics['outcome_count'].sum())*100),2)}%")
k4.metric('Data Coverage percentage',f"{round(((report_df_metrics['outcome_count'].count()/report_df['outcome_count'].count())*100),2)}%")

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
        filtered_count = filtered_df.head(selected_count)
    else:
        filtered_count = filtered_df
    

st.markdown("<br><br>", unsafe_allow_html=True)    


bar_chart_data = filtered_count.pivot(
        index = 'campaign',
        values = 'outcome_count',
        columns = 'outcome'
    )

st.bar_chart(bar_chart_data)

st.button('Download')

