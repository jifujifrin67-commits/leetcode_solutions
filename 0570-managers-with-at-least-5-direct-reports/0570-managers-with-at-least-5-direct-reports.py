import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    ans = pd.merge(employee, employee["managerId"].value_counts(), how="left", left_on="id", right_on="managerId")
    filt = (ans["count"] >= 5)
    return ans[filt][["name"]]