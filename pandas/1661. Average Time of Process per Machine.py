import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(activity, activity, on=["machine_id", "process_id"])
    res = res[(res["activity_type_x"] == "start") & (res["activity_type_y"] == "end")]
    res["processing_time"] = res["timestamp_y"] - res["timestamp_x"]
    res = res[["machine_id", "process_id", "processing_time"]]
    res = res.groupby(["machine_id"], as_index=False).mean()
    res = res[["machine_id", "processing_time"]]
    res["processing_time"] = res["processing_time"].apply(lambda x: round(x, 3))
    return res
