import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank']= scores['score'].rank(method='dense',ascending=False).astype(int)
    # method='dense' ayni skorlarin ayni rank i almasi icin kullanilir.

    return scores.sort_values(by='score',ascending=False)[['score','rank']]

scores = pd.DataFrame({
    'id': [1,2,3,4,5,6],
    'score': [3.50,3.65,4.00,3.85,4.00,3.65]
})

print(order_scores(scores))
