from utils.styling import apply_background
import streamlit as st
from database.auth import logout
from utils.logger import logger

apply_background('utils/background.jpg')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page('app.py')
    st.stop()

# st.write("Profile State")
# st.write(dict(st.session_state))

if st.session_state.logged_in:
    # st.write(st.session_state.user_role)
    # st.write(st.session_state.reports_to_view)
    # st.write(st.session_state.reports_to_download)

    st.title('Dashboard Homepage')

    st.markdown("<br>", unsafe_allow_html=True)
     

    Reports = {
        "campaign_overview": { 'title': 'Campaign Overview',
                              'desc': ('High level campaign overview'
                                  'and distribution analysis'),
                              'page' : 'pages/campaign_overview.py'},
        "customer_segmentation": {'title' : 'Customer Segmentation',
                                  'desc' : ('High level customer segmentation'
                                            'and distribution analysis'),
                                  'page': 'pages/customer_segmentation.py'},
        "campaign_effectiveness": {'title' : 'Campaign Effictiveness',
                                   'desc': ('Conversion analysis and '
                                         'campaign effectiveness metrics'),
                                   'page': 'pages/campaign_effectiveness.py'},
        "cpg_cus_affinity":{'title' : 'Campaign Customer Affinity',
                            'desc' : ('Customer segmentation and '
                                     'campaign affinity analysis'),
                            'page' : 'pages/cpg_cus_affinity.py'}
    }    

    for report in st.session_state.reports_to_view:

        config = Reports[report]

        with st.container(border = True):

            st.subheader(config['title'])
            st.write(config['desc'])
            
            if st.button('Open Report', key = report):
                logger.info(f'User {st.session_state.username} is accessing the report {config['title']}')
                st.switch_page(config['page'])


    with st.sidebar: 
        if st.button('Logout'):
            logger.info(f'User {st.session_state.username} logged out')
            logout()       

