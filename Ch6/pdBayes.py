"""
@author: jordan
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
from random import shuffle
from math import exp, pi, sqrt
from pprint import pprint
datapath = "mpg.csv"
numbuckets = 10;
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
def calcProbs(df):
    classProb={}
    for name in classNames:
        classProb[name] = {}
    for col in df.columns:
        if col!="class" and col!="bucket":
            levels = len(df[col].value_counts());
            #if(levels<10): Assuming that these cols are non-discrete
            if df[col].dtype not in numerics or levels<5:
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
                    classProb[cname][col] = {"mean": mean[cname], "sd": std[cname]}
    return classProb;
def classify(testCase, prob, priorProb):
    posteriors = {};
    #pprint(testCase)
    for className in priorProb.keys():
        posteriors[className] = priorProb[className]
        for (cname, attr) in testCase.iteritems():
            if(cname not in ("class", "bucket")):
                if("mean" in prob[className][cname]):
                    mean = prob[className][cname]["mean"]
                    sd = prob[className][cname]["sd"]
                    posteriors[className]*=exp((-1*(attr-mean)**2)/2*sd**2)/(sqrt(2*pi)*sd)
                else:
                    try:
                        posteriors[className]*=prob[className][cname][attr]
                    except:
                        print("Error:"+cname+" "+str(attr))
    return max(posteriors, key=posteriors.get);
df = pd.read_csv(datapath);
df['bucket'] = np.random.randint(0, numbuckets, len(df))
accuracies = [];
for bucketnum in range(numbuckets):
    totalTest=0;
    totalCorrect=0;
    testData = df[df["bucket"]==bucketnum]
    trainingData = df[df["bucket"]!=bucketnum]
    numobs = trainingData["class"].size;
    classCounts = trainingData["class"].value_counts();
    priorProb = classCounts/numobs;
    classNames = priorProb.keys().values
    prob = calcProbs(trainingData);
    for (index, row) in testData.iterrows():
        if row["class"] == classify(row, prob, priorProb):
            totalCorrect+=1;
        totalTest+=1
    accuracy = totalCorrect*100.0/totalTest
    print("Prediction acccuracy: "+str(accuracy)+"%")
    accuracies.append(accuracy);
repAccuracy = sum(accuracies)/numbuckets;
print("Rep accuracy: "+str(repAccuracy)+"%");