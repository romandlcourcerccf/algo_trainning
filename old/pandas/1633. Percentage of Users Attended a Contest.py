import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(register, users, on=["user_id"]).sort_values(by="contest_id")
    res.drop(["user_name"], inplace=True, axis=1)

    res = res.groupby("contest_id").agg("count").reset_index()
    res["percentage"] = ((res["user_id"] / users["user_id"].nunique()) * 100).round(2)
    res.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True], inplace=True
    )
    res.drop("user_id", inplace=True, axis=1)
    return res


import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby("contest_id").agg("count").reset_index()
    df["percentage"] = round(df["user_id"] / len(users) * 100, 2)
    df = df.sort_values(by=["percentage", "contest_id"], ascending=[False, True])
    return df[["contest_id", "percentage"]]
