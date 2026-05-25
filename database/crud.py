from database.db import User,engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
import bcrypt as b
from utils.logger import logger

Session = sessionmaker(bind = engine)



#Function to add user to the system
def add_users(nm,usnm,pswd):
    session  = Session()
    try:    
        if (nm and usnm and pswd):
            hash_pswd = b.hashpw(
                 pswd.encode('utf-8'),
                 b.gensalt()
             ).decode('utf-8')
            user = User(name = nm,username = usnm.lower(),password =hash_pswd)
            session.add(user)
            session.commit()
            logger.info(f'User {nm} created successfully in the system')
            return {
                "success": True,
                "message": "User created successfully"
            }
    except IntegrityError as e:
        logger.exception(f'IntegrityError, {e}')
        session.rollback()
        return {
            "success": False,
            "message": "Username already exists"
        }
    except Exception as e:
        logger.exception(f'Something failed,{e}')
        session.rollback()
        return {
            "success": False,
            "message": str(e)
        }
    finally:
        session.close()


#Function to read user from the system
def get_users_by_username(usnm):
    session  = Session()
    try:
        if usnm:
            user = session.query(User).filter_by(username = usnm.lower()).first()
            logger.info(f"User found in the system, {usnm}")
            return user
    except Exception as e:
        logger.exception(f'Invalid user: {e}')
        return None
    finally:
        session.close()
    
#Function to update user password 
def update_user_password(usnm,pswd):
    session  = Session()
    try:
        if usnm:
            user = session.query(User).filter_by(username = usnm.lower()).first()

            if not user:
                return False

            user.password = b.hashpw(
                 pswd.encode('utf-8'),
                 b.gensalt()
             ).decode('utf-8')
            session.commit()
            logger.info(f'Password for user {usnm} has been updated')
            return True
    except Exception as e:
        session.rollback()
        logger.exception(f'Invalid user : {e}')
        return False
    finally:
        session.close()
    
    
#Function to delete user from the system
def remove_user(usnm):
    session  = Session()
    try:
        if usnm: 
            user = session.query(User).filter_by(username = usnm.lower()).first() 

            if not user:
                return False

            session.delete(user)
            session.commit()
            logger.info(f'User {usnm} has been deleted')
            return True
    except IntegrityError as e:
        session.rollback()
        logger.exception(f'Cannot delete user: {e}')
        return False
    finally:
        session.close()
 
            

    




