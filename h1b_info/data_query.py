import pandas as pd

def queryData(start=0, end= 50, name = '', sort_col='h1b_score', ascending = False):
    df = pd.read_csv('./h1b_info/data/transformed_data.csv')
    df.fillna('')
    if name:
        df = df[df['name'].str.contains('SNAPCH')]
    df = df[start:end]
    if sort_col:
        df = df.sort_values(by=sort_col, ascending=ascending)
    return df[['id', 'name', 'lca_score', 'h1b_score', 'lca_confidence', 'h1b_confidence', 'lca_max_salary', 'h1b_uscis_status']]

def getData(start=0, end= 50, name = '', sort_col='h1b_score', ascending = False):
    df = queryData(start, end, name, sort_col, ascending)
    json_data = df.to_json(orient='records')  # Convert DataFrame to JSON string
    return json_data

print(getData())

