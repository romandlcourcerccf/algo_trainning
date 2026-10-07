import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    ws = weather.sort_values("recordDate", ascending=True)
    ws["td"] = ws["temperature"].diff()
    ws["dd"] = ws["recordDate"].diff().dt.days
    return ws[(ws["td"] > 0) & (ws["dd"] == 1)][["id"]]


import pandas as pd
import datetime


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    ## first sort data
    weather.sort_values(by="recordDate", inplace=True)
    ind = (weather["temperature"].diff() > 0) & (
        weather["recordDate"].diff().dt.days == 1
    )
    return weather.loc[ind, ["id"]]
