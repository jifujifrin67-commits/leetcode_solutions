import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores["rank"] = scores.score.rank(
                     method = "dense", ascending=False)

    return scores.iloc[:,[1,2]].sort_values("rank")