import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    df  = pd.merge(product, sales, on=['product_id'])[['product_name', 'year', 'price']]
    return df
    