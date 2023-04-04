import pandas as pd

merge = ['Jumping_phone_pocket_cg.csv', 'file2.csv']
df = pd.DataFrame()
for file in merge:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
df.to_csv('jumping_cg.csv', index=False)