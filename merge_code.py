import pandas as pd

#adding flags to later determine what is considered jumping and walking and whos data is whos
#this will help with the metadata and division of time segments in later steps 
jumpCG = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_cg.csv')
jumpHC = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_hc.csv')
jumpLP = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_lp.csv')

jumpCG['person'] = 0
jumpHC['person'] = 1
jumpLP['person'] = 2

jumpCG['method'] = 0
jumpHC['method'] = 0
jumpLP['method'] = 0

jumpCG.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_cg.csv')
jumpHC.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_hc.csv')
jumpLP.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/jumping_lp.csv')

merge1 = ['C:/Users/Cassie G/Documents/390FinalProject-1/jumping_cg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/jumping_hc.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/jumping_lp.csv'
         ]

data_frame1 = pd.DataFrame()

for csv1 in merge1:
    data1 = pd.read_csv(csv1)
    data_frame1 = pd.concat([data_frame1, data1], axis=0)

data_frame1.to_csv('allJump.csv', index=False)


walkCG = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_cg.csv')
walkHC = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_hc.csv')
walkLP = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_lp.csv')

walkCG['person'] = 0
walkHC['person'] = 1
walkLP['person'] = 2

walkCG['method'] = 0
walkHC['method'] = 0
walkLP['method'] = 0

walkCG.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_cg.csv')
walkHC.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_hc.csv')
walkLP.to_csv('C:/Users/Cassie G/Documents/390FinalProject-1/walking_lp.csv')

merge2 = ['C:/Users/Cassie G/Documents/390FinalProject-1/walking_cg.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/walking_hc.csv',
         'C:/Users/Cassie G/Documents/390FinalProject-1/walking_lp.csv'
         ]

data_frame2 = pd.DataFrame()

for csv2 in merge2:
    data2 = pd.read_csv(csv2)
    data_frame2 = pd.concat([data_frame2, data2], axis=0)

data_frame2.to_csv('allWalk.csv', index=False)
