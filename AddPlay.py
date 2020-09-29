import numpy as np
import pandas as pd
#this is used for setting up each csv for us to be able to use it properly
data = pd.read_csv("C:/python/baseball/in/2014Pitching.csv")
#create an array of the teams who made playoffs
#name has to correspond to how the name was written in the csv
#2019 ["MIL","WSN","TBR","OAK","STL","LAD","MIN","NYY","ATL","HOU"]
#2018 ["BOS","LAD","MIL","HOU","NYY","CLE","COL","OAK","ATL","CHC"]
#2017 ["WSN","CHC","ARI","LAD","BOS","HOU","NYY","CLE","MIN","COL"]
#2016 ["LAD","WSN","CHC","SFG","CLE","TEX","TOR","TEX","BAL","NYM"]
#2015 ["NYM","LAD","CHC","STL","TOR","TEX","KCR","HOU","NYY","PIT"]
#2014 ["STL","LAD","SFG","WSN","BAL","DET","KCR","LAA","OAK","PIT"]
teams = ["STL","LAD","SFG","WSN","BAL","DET","KCR","LAA","OAK","PIT"]
data["post"] = 0
for index, rows in data.iterrows():
    name = data.at[index,'Tm']
    for i in teams:
        if i == name:
            data.at[index,'post'] = 1
data = data.drop([30,31])
data.to_csv("C:/python/baseball/out/2014Pitching.csv")
