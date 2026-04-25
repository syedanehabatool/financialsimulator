import pandas as pd

def load_data():
    df = pd.read_csv('data.csv')
    df = df.rename(columns={df.columns[0]: 'Year'})
    df['Year'] = pd.to_datetime(df['Year']).dt.year
    return df