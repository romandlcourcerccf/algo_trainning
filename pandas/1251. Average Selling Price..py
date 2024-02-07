import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    res = pd.merge(prices, units_sold, on=['product_id'], how='left')
    res = res[(res['purchase_date'] >= res['start_date']) & (res['purchase_date'] <= res['end_date']) | pd.isna(res['purchase_date'] )]
    res = (res['price'] * res['units']).groupby(res['product_id']).sum() / res['units'].groupby(res['product_id']).sum()
    res = res.to_frame().reset_index()
    res = res.rename(columns={0: "average_price"})
    res['average_price'] = res['average_price'].round(2)
    res['average_price'] = res['average_price'].apply(lambda x: 0 if x is None else x)
    res = res.fillna(0)

    return res


