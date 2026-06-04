import pandas as pd
from sqlalchemy import create_engine,text
from database.queries import get_customer_segmnet_query

engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')

def get_customer_segment():

    data = pd.read_sql(text(get_customer_segmnet_query), engine)

    data = data.sort_values(by='avg_salary', ascending=False)

    return data

