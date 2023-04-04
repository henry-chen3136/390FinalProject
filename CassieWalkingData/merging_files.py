import pandas as pd

merge1 = ['C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/JumpingPhonePocketcg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/jumpingcg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/jumpingPhoneHandcg.csv'
         ]

data_frame1 = pd.DataFrame()

for csv1 in merge1:
    data1 = pd.read_csv(csv1)
    data_frame1 = pd.concat([data_frame1, data1], axis=0)

data_frame1.to_csv('jumping_cg.csv', index=False)

merge2 = ['C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/walkingHandcg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/walkingHoodiePocketcg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/CassieData/WalkingPhonePocketcg.csv'
         ]

data_frame2 = pd.DataFrame()

for csv2 in merge2:
    data2 = pd.read_csv(csv2)
    data_frame2 = pd.concat([data_frame2, data2], axis=0)

data_frame2.to_csv('walking_cg.csv', index=False)