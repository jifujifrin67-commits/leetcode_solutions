import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee['salary'].nunique() < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    second_highest = employee['salary'].drop_duplicates().nlargest(2).iloc[-1]
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})