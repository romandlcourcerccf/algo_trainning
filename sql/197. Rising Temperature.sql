# Write your MySQL query statement below
-- select w1.id from Weather as w1
-- where w1.temperature > (select temperature from Weather where recordDate = w1.recordDate-1)


select w1.id
from Weather w1, Weather w2
where w1.temperature > w2.temperature  and DATEDIFF( w1.recordDate, w2.recordDate) = 1


select w1.id
from Weather w1, Weather w2
where w1.temperature > w2.temperature  and DATE_PART('day', w1.recordDate) - DATE_PART('day', w2.recordDate) = 1



import pandas as pd
import datetime

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    ## first sort data
    weather.sort_values(by='recordDate', inplace=True)
    ind = (weather['temperature'].diff() > 0) & (weather['recordDate'].diff().dt.days == 1)
    return weather.loc[ind, ['id']]