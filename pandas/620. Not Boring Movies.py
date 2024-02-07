import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    
    df = cinema[(cinema['id'] % 2 !=0) & (cinema['description'] != 'boring')]
    df = df.sort_values(['rating'], ascending=False)
    return df