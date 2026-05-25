import bcrypt as b
# from db import User,engine
from database.crud import get_users_by_username
import streamlit as st
from utils.logger import logger




# session = Session()

# users = session.query(User).all()

# for user in users:
#     db_pswd = user.password
#     hash_pswd = b.hashpw(
#         db_pswd.encode('utf-8'),
#         b.gensalt()
#     ).decode('utf-8')

#     user.password = hash_pswd

# session.commit()


def verify_user(usnm,pswd):
    try:
        user = get_users_by_username(usnm.lower())

        if not user and not pswd:
            return False
        
        return b.checkpw(
            pswd.encode('utf-8'),
            user.password.encode('utf-8')
        )
    except Exception as e:
        logger.exception(f'Something went wrong, {e}')
        return False
    

def login_check(usnm, pswd):
    if usnm and pswd:
        if verify_user(usnm, pswd):
            st.session_state.logged_in = True
            logger.info(f'Login successful for user, {usnm}')
            return True
        else:
            logger.error(f'Failed login for user, {usnm}')
            return False

def logout():
   logger.info(f'Logout successful')
   st.session_state.logged_in = False
   st.switch_page('app.py')
   return True