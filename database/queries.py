get_campaign_overview_query = """select campaign,
case when poutcome not in ('failure','success') then 'NA' else poutcome end as outcome,
count(*) as outcome_count
from bank_marketing 
group by case when poutcome not in ('failure','success') then 'NA' else poutcome end ,campaign"""