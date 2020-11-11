import numpy as np
import pandas as pd
#combining all of the created csv's to get a bigger data set

data11 = pd.read_csv("out/2009PitchingBatting.csv")
data10 = pd.read_csv("out/2010PitchingBatting.csv")
data9 = pd.read_csv("out/2011PitchingBatting.csv")
data8 = pd.read_csv("out/2012PitchingBatting.csv")
data7 = pd.read_csv("out/2013PitchingBatting.csv")
data6 = pd.read_csv("out/2014PitchingBatting.csv")
data5 = pd.read_csv("out/2015PitchingBatting.csv")
data4 = pd.read_csv("out/2016PitchingBatting.csv")
data3 = pd.read_csv("out/2017PitchingBatting.csv")
data2 = pd.read_csv("out/2018PitchingBatting.csv")
data1 = pd.read_csv("out/2019PitchingBatting.csv")
frames = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11]
result = pd.concat(frames)
result.to_csv("LargePitchingBatting.csv")

