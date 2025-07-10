import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.copy()
    scores['rank'] = scores['score'].rank(
        method='dense', ascending=False).astype(int)
    return scores[['score', 'rank']].sort_values(by='score',ascending=False)

data = {
    "id": [1, 2, 3, 4, 5, 6],
    "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}
#pd.DataFrame({'score':[scores['score'].sort_values(ascending=False)],
#                         'rank':ranked['rank']})
scores = pd.DataFrame(data)
print(order_scores(scores))