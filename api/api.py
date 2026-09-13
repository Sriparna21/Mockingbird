from fastapi import FastAPI
from pydantic import BaseModel
from report_service.campaign_overview import (get_campaign_overview)
from report_service.campaign_effectiveness import (get_campaign_effectiveness)
from report_service.cpg_cus_affinity import (get_affinity)
from report_service.customer_segmentation import (get_customer_segment)

app = FastAPI()

class CampaignOverview(BaseModel):
    campaign : int
    outcome : str
    outcome_count : int

@app.get('/campaign/overview',response_model=list[CampaignOverview])
def campaign_overview_api():
    data = get_campaign_overview()
    return data.to_dict(orient="records")

class CampaignEffectiveness(BaseModel):
    campaign : int
    outcome : str
    outcome_count : int


@app.get('/campaign/effectiveness', response_model=list[CampaignEffectiveness])
def campaign_effectiveness_api():
    data = get_campaign_effectiveness()
    return(data.to_dict(orient='records'))



class CampaignAffinity(BaseModel):
    job : str
    campaign : int
    poutcome : str
    avg_balance : float
    customer_count : int


@app.get('/campaign/affinity', response_model=list[CampaignAffinity])
def campaign_affinity_api():
    data = get_affinity()
    return(data.to_dict(orient='records'))


class CampaignSegmentation(BaseModel):
    id : int
    job : str
    marital : str
    housing : str
    avg_salary : float
    campaign : int


@app.get('/campaign/segmentation', response_model=list[CampaignSegmentation])
def campaign_segmentation_api():
    data = get_customer_segment()
    return(data.to_dict(orient='records'))