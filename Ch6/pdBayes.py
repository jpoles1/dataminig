"""
@author: jordan
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
from random import shuffle
from pprint import pprint
datapath = "hv.csv"
numbuckets = 10;
df = pd.read_csv(datapath);
df['buckets'] = np.random.randint(0, numbuckets, len(df))
print df["buckets"].value_counts();
df['age'] = np.random.rand(len(df))*80;
numobs = df["class"].size;
classCounts = df["class"].value_counts();
priorProb = classCounts/numobs;
classProb = {}
classNames = priorProb.keys().values
for name in classNames:
    classProb[name] = {}
print classNames
for col in df.columns:
    if col!="class":
        levels = len(df[col].value_counts());
        if(levels<10): #Assuming that these cols are non-discrete
            attrCounts = df.groupby("class")[col].value_counts(normalize=1);
            for ((cname, attr), value) in attrCounts.iteritems():
                if(col not in classProb[cname]):
                    classProb[cname][col] = {}
                classProb[cname][col][attr] = value
        else:
            group = df.groupby("class")[col];
            mean = group.mean().to_dict()
            std = group.std().to_dict()
            for cname in classNames:
                classProb[cname][col] = {"mean": mean[cname], "std": std[cname]}