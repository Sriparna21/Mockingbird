import streamlit as st
from utils.styling import apply_background
from report_service.customer_segmentation import (get_customer_segment)
import plotly.express as px

st.set_page_config(layout="wide")
apply_background('utils/background.jpg')

st.title('Customer Segmentation')
st.markdown("<br>", unsafe_allow_html=True)


st.write('This is a summary report detailing customer insights.')

# st.markdown("<br>", unsafe_allow_html=True)

report_df = get_customer_segment()
#st.dataframe(report_df)

k1,k2,k3,k4= st.columns(4)

k1.metric('Average salary of the customers',f'${round(report_df.avg_salary.mean(),2)}')
k2.metric('Higest salary of the group', f'${report_df.avg_salary.max()}')


k3.metric('Total premium customers', report_df[report_df.avg_salary >= report_df.avg_salary.mean()].shape[0])
k4.metric('Most common job of the customers', report_df.job.mode()[0].title())

st.markdown("<br><br>", unsafe_allow_html=True)

chart_container = st.container()
col1,col2 = st.columns(2)

with col1:
    outcome_mapping = {
            'Job status': 'job',
            'Marital status': 'marital',
            'Housing status': 'housing',
            'Campaign': 'campaign'
        }

    # st.subheader(f'What perspective would you like to see?')
    selected_perspective = st.selectbox('Analysis viewpoint',outcome_mapping.keys())

with col2:
    # st.subheader('Select your chart')
    chart = st.selectbox('Select your chart',['Bar','Pie','Line'])

# st.markdown("<br><br>", unsafe_allow_html=True)

cp = (report_df.groupby(outcome_mapping[selected_perspective])['id'].count().reset_index(name= 'customer_count'))

with chart_container:
    st.subheader(f'Customer distribution by {selected_perspective}')

if chart == 'Bar':
    # st.bar_chart(cp , x = outcome_mapping[selected_perspective], y = 'customer_count')
    fig = px.bar(cp, x = outcome_mapping[selected_perspective],y = 'customer_count', text = 'customer_count')
    st.plotly_chart(fig,use_container_width=True)
elif chart == 'Line':
    # st.line_chart(cp , x = outcome_mapping[selected_perspective], y = 'customer_count')
    fig = px.line(cp, x = outcome_mapping[selected_perspective],y = 'customer_count', text = 'customer_count')
    st.plotly_chart(fig,use_container_width=True)
else:
    fig = px.pie(cp, values = 'customer_count', names = outcome_mapping[selected_perspective])
    st.plotly_chart(fig,use_container_width=True)


with st.expander("View Raw Data"):

    st.dataframe(cp)

st.download_button(
    label = 'Download Report',
    data = cp.to_csv(index=False),
    file_name = f'Customer_Segmentation_Report_By_'
    f'{selected_perspective.replace(" ","_")}.csv',
    mime='text/csv'
)

