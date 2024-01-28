import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(visits, transactions, on=['visit_id'],  how='left')
    df = df[df['transaction_id'].isna()].groupby('customer_id').count()
    df = df.reset_index()
    df['count_no_trans'] = df['visit_id']
    df = df[['customer_id', 'count_no_trans']]
    return df
