import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, bonus, on=["empId"], how="left")
    df = df[(df["bonus"] < 1000) | (df["bonus"].isnull())][["name", "bonus"]]
    return df
