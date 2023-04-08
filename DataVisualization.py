import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#importing data
jump = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/allJump.csv')
walk = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/allWalk.csv')
both = pd.read_csv('C:/Users/Cassie G/Documents/390FinalProject-1/datasetOverall.csv')

#renaming the columns in the dataset so it is easier to call 
jump = jump.rename(columns={"Time (s)" : "time", "Linear Acceleration x (m/s^2)" : "x", 
                     "Linear Acceleration y (m/s^2)" : "y", "Linear Acceleration z (m/s^2)" : "z", 
                     "Absolute acceleration (m/s^2)" : "abs"})

walk = walk.rename(columns={"Time (s)" : "time", "Linear Acceleration x (m/s^2)" : "x", 
                     "Linear Acceleration y (m/s^2)" : "y", "Linear Acceleration z (m/s^2)" : "z", 
                     "Absolute acceleration (m/s^2)" : "abs"})

both = both.rename(columns={"Time (s)" : "time", "Linear Acceleration x (m/s^2)" : "x", 
                     "Linear Acceleration y (m/s^2)" : "y", "Linear Acceleration z (m/s^2)" : "z", 
                     "Absolute acceleration (m/s^2)" : "abs"})


#plotting x and z variables within each dataset to compare
jumpXZ = plt.scatter(jump.loc[:,["x"]], jump.loc[:,["z"]])

plt.show()

walkXZ = plt.scatter(walk.loc[:,["x"]], walk.loc[:,["z"]])
plt.show()

bothXZ = plt.scatter(both.loc[:,["x"]], both.loc[:,["z"]])
plt.show()

plt.tight_layout()

