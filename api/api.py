from fastapi import FastAPI
from pydantic import BaseModel
from report_service.campaign_overview import (get_campaign_overview)
from report_service.campaign_effectiveness import (get_campaign_effectiveness)
from report_service.cpg_cus_affinity import (get_affinity)
from report_service.customer_segmentation import (get_customer_segment)
from prediction.prediction_service import predict_customer,initialize_model

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


class CustomerPredictionRequest(BaseModel):
    age : int
    job : str
    marital : str
    education : str
    housing : str
    loan : str
    campaign : int
    pdays : int
    deposit : str
    balance : int

class Factors(BaseModel):
    Feature_name : str
    Feature_value : str | int | float
    Contribution : float
    Direction : str
class CustomerPredictionResponse(BaseModel):
    prediction : str
    failure_probability : float
    success_probability : float
    success_factors : list[Factors]
    failure_factors : list[Factors]

preprocessor, model = initialize_model()

@app.post('/campaign/predict', response_model=CustomerPredictionResponse)
def campaign_prediction_api(customer : CustomerPredictionRequest):
    result,success_factors,failure_factors = predict_customer(customer.model_dump(),preprocessor,model)

    return {'prediction' : result['prediction'],
        'failure_probability' : result['failure_probability'],
        'success_probability' : result['success_probability'],
        'success_factors' : success_factors,
        'failure_factors' : failure_factors}
