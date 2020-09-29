import numpy as np
import pandas as pd
#combining all of the created csv's to get a bigger data set
data1 = pd.read_csv("C:/python/baseball/out/2014Pitching.csv")
data2 = pd.read_csv("C:/python/baseball/out/2015Pitching.csv")
data3 = pd.read_csv("C:/python/baseball/out/2016Pitching.csv")
data4 = pd.read_csv("C:/python/baseball/out/2017Pitching.csv")
data5 = pd.read_csv("C:/python/baseball/out/2018Pitching.csv")
data6 = pd.read_csv("C:/python/baseball/out/2019Pitching.csv")
frames = [data1,data2,data3,data4,data5,data6]
result = pd.concat(frames)
result.to_csv("LargeTest.csv")

