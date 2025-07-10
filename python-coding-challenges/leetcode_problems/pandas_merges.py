import pandas as pd

def pivot_table(df):
    pivoted = pd.pivot_table(df,
                   index='Store',
                   columns=['Month', 'Product'],
                   values='Sales',
                             aggfunc=['sum', 'mean', 'count'])
    return pivoted


data = {
    'Store': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B'],
    'Month': ['Jan', 'Feb', 'Mar'] * 4,
    'Product': ['Apples'] * 6 + ['Bananas'] * 6,
    'Sales': [100, 120, 130, 90, 110, 115, 80, 90, 95, 70, 75, 78]
}

df = pd.DataFrame(data)

print(pivot_table(df))