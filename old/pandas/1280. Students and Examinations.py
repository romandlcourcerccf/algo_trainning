import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    df1 = pd.merge(students, subjects, how="cross")
    df1["attended_exams"] = df1.apply(
        lambda row: len(
            examinations[
                (examinations["student_id"] == row["student_id"])
                & (examinations["subject_name"] == row["subject_name"])
            ]
        ),
        axis=1,
    )
    df1 = df1.sort_values(["student_id", "subject_name"])
    return df1


import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    temp = students.merge(subjects, how="cross")
    exam = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index(name="attended_exams")
    )
    ans = temp.merge(exam, how="left", on=["student_id", "subject_name"]).sort_values(
        by=["student_id", "subject_name"]
    )
    ans["attended_exams"].fillna(0, inplace=True)
    return ans[["student_id", "student_name", "subject_name", "attended_exams"]]
