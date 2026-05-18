import bcrypt as b
# from db import User,engine
from database.crud import get_users_by_username
from sqlalchemy.orm import sessionmaker



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
        print(f'Something went wrong, {e}')
        return False
    
