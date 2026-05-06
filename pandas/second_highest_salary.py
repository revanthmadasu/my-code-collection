'''
    problem: https://leetcode.com/problems/second-highest-salary/
    concepts: dataframes, sorting, drop_duplicates
'''
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[["salary"]].drop_duplicates()
    df = df.sort_values("salary", ascending=False)
    return pd.DataFrame({
        "SecondHighestSalary": [df.iloc[1]["salary"] if len(df) > 1 else None]
        })