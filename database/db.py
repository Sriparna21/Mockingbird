# from sqlalchemy import create_engine,text
# from sqlalchemy.exc import IntegrityError,SQLAlchemyError


# engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')


# # Create a user through the app
# def add_users(usr, pwd):
#     try:
#         with engine.begin() as conn:
#             query = text('insert into users (Username, Password) values (:usr, :pwd)')
#             result = conn.execute(query, {"usr": usr, "pwd": pwd})

#             if result.rowcount > 0:
#                 return True
#             else:
#                 return False
#     except IntegrityError as e:
#         print("User already exists or constraint violated, please check")
#         return False
        

# # Fetch all users for the app
# def fetch_all_users():
    
#     with engine.connect() as conn:
#         query = text('select * from users')

#         result = conn.execute(query)

#         data = result.mappings().all()

#         return data
    


# # Fetch user by the username
# def fetch_users_by_username(usr):
#     try:
#         with engine.connect() as conn:
#             query = text('select * from users where username= :usr')
#             result = conn.execute(query,{'usr':usr})
#             data = result.mappings().first()

#             if data:
#                 return data
#     except Exception as e:
#         print("Invalid user ,{e}")  
#         return None


# # Delete user
# def remove_user(usr):
#     try:
#         with engine.begin() as conn:
#             query = text('delete from users where username = :usr')
#             result = conn.execute(query,{'usr':usr})

#             if result.rowcount > 0:
#                 return True
#     except SQLAlchemyError as e:
#         print("Invalid user: {e}")  
#         return False
    
# #Update password for the user
# def update_user_pswd(usr,pswd):
#     try:
#         with engine.begin() as conn:
#             query = text('update users set password = :pswd where username = :usr')
#             result = conn.execute(query,{'usr':usr,'pswd':pswd})

#             if result.rowcount > 0:
#                 return True
#     except Exception as e:
#         print("Invalid user: {e}")  
#         return False
    


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')

base = declarative_base()

#Creating table users_orm 
class User(base):
    __tablename__ = 'users_orm'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String,unique = True)
    password = Column(String)

base.metadata.create_all(engine)
