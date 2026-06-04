from utils.styling import apply_background
from database.auth import logout
import streamlit as st

apply_background('utils/background.jpg')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page('app.py')

if st.session_state.logged_in:

    st.title('Profile')

    st.write(f'Welcome, {st.session_state.name}')
   
    with st.container(border = True):
        st.subheader(f'User information for {st.session_state.name}')

        st.write(f'Username : {st.session_state.username}')
        st.markdown("<br>", unsafe_allow_html=True)
        st.metric(f'Your role is : {st.session_state.user_role}')
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(f'Reports you have access to : ')

        Reports = {
        "campaign_overview":  'Campaign Overview',
                              
        "customer_segmentation": 'Customer Segmentation',
                                  
        "campaign_effectiveness": 'Campaign Effictiveness',
                                  
        "cpg_cus_affinity":'Campaign Customer Affinity',
                            
        }    


        for report in st.session_state.reports_to_view:
            st.write(f'📊 {Reports[report]}')

    if st.button('Go to Dashboard'):
        st.switch_page('pages/2_dashboard.py')


    
    with st.sidebar: 
        if st.button('Logout'):
            logout()