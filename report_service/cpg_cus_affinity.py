import pandas as pd
from sqlalchemy import create_engine,text
from database.queries import get_affinity_query

engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')

def get_affinity():

    data = pd.read_sql(text(get_affinity_query), engine)

    data = data.sort_values(by='customer_count', ascending=False)

    return data

