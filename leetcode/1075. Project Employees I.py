import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    res = pd.merge(project, employee, on='employee_id', how='inner').groupby('project_id').mean('experience_years').reset_index()
    res['average_years'] = res['experience_years']
    res = res.drop(columns=['employee_id', 'experience_years'])
    res = res.round(2)
    return res
