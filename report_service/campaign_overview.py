import pandas as pd
from sqlalchemy import create_engine,text
from database.queries import get_campaign_overview_query

engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')

def get_campaign_overview():

    data = pd.read_sql(text(get_campaign_overview_query), engine)

    data = data.sort_values(by='campaign')

    return data

