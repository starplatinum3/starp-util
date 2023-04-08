import pandas as pd
pandas_engine='pandas'
pyspark_engine='pyspark'
engine='pandas'
def join(df1,df2,on):
    if engine==pandas_engine:
        return df1.join(df2,on=on)
    return df2.join(df1, on=on)

def joindemo():
    age_df = pd.DataFrame({'name': ['lili', 'lucy', 'tracy', 'mike'],
                           'age': [18, 28, 24, 36]})
    score_df = pd.DataFrame({'name': ['tony', 'mike', 'akuda', 'tracy'],
                             'score': ['A', 'B', 'C', 'B']})
# ValueError: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
    result = age_df.join(score_df, on='name')
    print(result)

joindemo()