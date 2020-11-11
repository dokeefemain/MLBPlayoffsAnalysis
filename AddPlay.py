import numpy as np
import pandas as pd
#this is just adding playoffs to all of the data in input
inputf = "in/"
inputb = "Pitching.csv"
outb = "PitchingBatting.csv"
outf = "out/"
teamsAll =  [["MIL","WSN","TBR","OAK","STL","LAD","MIN","NYY","ATL","HOU"],["BOS","LAD","MIL","HOU","NYY","CLE","COL","OAK","ATL","CHC"],["WSN","CHC","ARI","LAD","BOS","HOU","NYY","CLE","MIN","COL"],["LAD","WSN","CHC","SFG","CLE","TEX","TOR","TEX","BAL","NYM"],
["NYM","LAD","CHC","STL","TOR","TEX","KCR","HOU","NYY","PIT"],["STL","LAD","SFG","WSN","BAL","DET","KCR","LAA","OAK","PIT"],["LAD","ATL","STL","PIT","DET","OAK","BOS","TBR","CLE","CIN"],["SFG","CIN","STL","WSN","OAK","DET","NYY","BAL","TEX","ATL"],
["MIL","ARI","STL","PHI","TEX","TBR","DET","NYY"],["SFG","ATL","PHI","CIN","NYY","MIN","TEX","TBR"],["PHI","COL","LAD","STL","LAA","BOS","NYY","MIN"]]
season = ["2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009"]

for j in range(len(season)):
    teams = teamsAll[j]
    pwd = inputf + season[j]+inputb
    data = pd.read_csv(pwd)
    data["post"] = 0
    for index, rows in data.iterrows():
        name = data.at[index,'Tm']
        for i in teams:
            if i == name:
                data.at[index,'post'] = 1
    data = data.drop([30,31])
    pwd = outf+season[j]+outb
    data.to_csv(pwd)
