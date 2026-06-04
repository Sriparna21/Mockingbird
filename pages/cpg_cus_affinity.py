import streamlit as st
from utils.styling import apply_background
from report_service.cpg_cus_affinity import (get_affinity)
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

if "cpg_cus_affinity" not in st.session_state.reports_to_view:
    logger.warning(f'User {st.session_state} does not have access to view the report - Customer_Campaign_Affinity')

st.title('Campaign Customer Affinity Report')
st.markdown("<br>", unsafe_allow_html=True)


st.write('This is a summary report detailing campaign to customer affinity relationships.')

report_df = get_affinity()
#st.dataframe(report_df)

k1,k2,k3,k4 = st.columns(4)

    
responsive_job = report_df[report_df.poutcome == 'success'].groupby('job').size().sort_values(ascending = False).index[0]
k1.metric('Most responsive job',responsive_job.title())

avg_bal_seg = report_df[report_df.poutcome == 'success'].groupby('avg_balance').size().sort_values(ascending = False).index[1]
k2.metric('Highest average balance in the segment',avg_bal_seg)

k3.metric('Conversion rate of customers',
          f"{round(((report_df[report_df['poutcome'] == 'success']['customer_count'].sum()/report_df['customer_count'].sum())*100),2)}%")
k4.metric('Rejection rate of customers',
          f"{round(((report_df[report_df['poutcome'] == 'failure']['customer_count'].sum()/report_df['customer_count'].sum())*100),2)}%")

st.divider()

col1, col2 = st.columns([6,2])

with col2:
    choice = st.toggle('Press toggle for successful outcomes')

with col1:
    if choice:
        fig = px.bar(
            report_df[report_df['poutcome'] == 'success'],
            x = 'job',
            y = 'customer_count',
            color = 'campaign',
            color_continuous_scale='Tealgrn'
        )

        st.plotly_chart(fig, use_container_width=True,config={'displayModeBar': False})

        st.download_button(
            label = 'Download Report',
            data = report_df[report_df['poutcome'] == 'success'].to_csv(index=True),
            file_name='Customer_Campaign_Affinity.csv',
            mime='text/csv'
            )

    else:
        fig = px.bar(
            report_df[report_df['poutcome'] == 'failure'],
            x = 'job',
            y = 'customer_count',
            color = 'campaign',
            color_continuous_scale='Reds'
        )

        st.plotly_chart(fig, use_container_width=True,config={'displayModeBar': False})

        if "cpg_cus_affinity" in st.session_state.reports_to_download:
            logger.info(f'User {st.session_state.username} is downloading the report - Customer_Campaign_Affinity')
            st.download_button(
                label = 'Download Report',
                data = report_df[report_df['poutcome'] == 'failure'].to_csv(index=True),
                file_name='Customer_Campaign_Affinity.csv',
                mime='text/csv'
                )

with st.sidebar: 
        if st.button('Logout'):
            logger.info(f'User {st.session_state.username} logged out')
            logout()       

        