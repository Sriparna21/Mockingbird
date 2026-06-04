import bcrypt as b
# from db import User,engine
from database.crud import get_users_by_username
import streamlit as st
from utils.logger import logger
from database.db import UserAccess,RoleAccess,engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)

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


def get_user_access(usnm):
    session = Session()
    try:
        if usnm:
            user = session.query(UserAccess).filter_by(username = usnm.lower()).first()
            access = user.access
            return access

    except Exception as e:
        st.error(f"ACCESS ERROR: {e}")
        logger.exception(f'No role found for the userr : {e}')
        return False
    finally:
        session.close()

def get_role_access(usnm):
    session = Session()
    try:
        if not usnm:
            return None
        else:
            user = session.query(UserAccess).filter_by(username = usnm.lower()).first()
            if not user:
                return None

            access = session.query(RoleAccess).filter_by(role = user.access).all()
            return access
    except Exception as e:
        st.error(f"ROLE ERROR: {e}")
        logger.exception(f'No access found for the user : {e}')
        return False
    finally:
        session.close()     


def verify_user(usnm,pswd):
    try:
        user = get_users_by_username(usnm.lower())

        if not user or not pswd:
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
            access = get_role_access(usnm)
            user = get_users_by_username(usnm.lower())

            st.session_state.logged_in = True
            st.session_state.username = usnm
            st.session_state.name = user.name
            st.session_state.user_role = get_user_access(usnm)
            st.session_state.reports_to_view = [r.report_name for r in access if r.can_view]
            st.session_state.reports_to_download = [r.report_name for r in access if r.can_download]
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

 
