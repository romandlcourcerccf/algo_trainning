import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    
    res = teacher.groupby('teacher_id').agg('nunique').reset_index()
    res.drop('dept_id', inplace=True, axis=1)
    res.rename(columns={'subject_id':'cnt'}, inplace=True)
    return res


import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    x = pd.DataFrame(teacher.groupby('teacher_id')['subject_id'].nunique()).reset_index()
    x.rename(columns = {'subject_id':'cnt'}, inplace=True)
    return x