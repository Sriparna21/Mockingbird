get_campaign_overview_query = """select campaign,
case when poutcome not in ('failure','success') then 'NA' else poutcome end as outcome,
count(*) as outcome_count
from bank_marketing 
group by case when poutcome not in ('failure','success') then 'NA' else poutcome end ,campaign"""


get_customer_segmnet_query = """ select c.id,c.job,c.marital,c.housing,avg(cg.balance) as Avg_Salary,cg.campaign
from customers c join campaign cg on cg.id = c.id 
group by c.id,c.job,c.marital,c.housing,cg.campaign """


get_campaign_effectiveness_query = """ select campaign, case when poutcome not in ('failure','success') then 'NA' else poutcome end as outcome,count(*) as outcome_count
from campaign 
group by campaign,case when poutcome not in ('failure','success') then 'NA' else poutcome end """