import pandas as pd

merge = ["JumpingPhonePocketcg.csv", "jumpingPhoneHandcg.csv", "jumpingcg.csv"]

data_frame = pd.DataFrame()

for csv in merge:
    data = pd.read_csv(csv)
    data_frame = pd.concat([data_frame, data], axis=0)

data_frame.to_csv('jumping_cg.csv', index=False)