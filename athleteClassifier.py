import csv
from math import sqrt
def manhattan(v1, v2):
    dist = 0;
    if(len(v1)==len(v2)):
        for i in range(len(v1)):
           dist+=abs(v1[i]-v2[i])
        return dist
    else:
        raise ValueError("Vectors not the same length")
def computeNeighbors(target, athletes):
    dists = {}
    for athlete in athletes:
        if(athlete!=target):
            dists[athlete] = manhattan(athletes[target], athletes[athlete])
    return sorted(dists, key=dists.get)
def classify(target, athletes, sports):
    dists = computeNeighbors(target, athletes)
    print dists
    return sports[dists[0]]
def standardize(athletes, standards):
    for athlete in athletes:
        for stat in range(len(athletes[athlete])):
            athletes[athlete][stat] = (athletes[athlete][stat] - standards[stat][0])/standards[stat][1]
    print athletes
def stscore(vect):
    sum = reduce(lambda x,y: x+y, vect)
    vect = sorted(vect)
    length = len(vect)
    if length%2!=0:
        median = (vect[length / 2] + vect[length / 2 - 1]) / 2.0
    else:
        median = vect[length / 2]
    stdev = sqrt(reduce(lambda x,y: x+y, [(x-median)**2 for x in vect])/length)
    return [median, stdev]
with open("athletesTrainingSet.txt") as datafile:
    reader = csv.reader(datafile, delimiter='	')
    athletes = {}
    sports = {}
    chars = []
    for i in range(len(reader.next())-2):
        chars.append([])
    for row in reader:
        for i in range(len(row)-2):
            chars[i].append(int(row[i+2]))
        sports[row[0]] = row[1]
        athletes[row[0]] = [int(row[2]), int(row[3])]
    standards = map(stscore, chars)
    standardize(athletes, standards)
    print classify("Brittainey Raven", athletes, sports)