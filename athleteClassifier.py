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

def euclidian(v1, v2):
    dist = 0;
    if(len(v1)==len(v2)):
        for i in range(len(v1)):
           dist+=(float(v1[i])-v2[i])**2
        return sqrt(dist)
    else:
        raise ValueError("Vectors not the same length")
def computeNeighbors(targetname, targetdata, athletes):
    dists = {}
    for athlete in athletes:
        if(athlete!=targetname):
            dists[athlete] = euclidian(targetdata, athletes[athlete])
    return sorted(dists, key=dists.get)
def classify(target, targetdata, athletes, sports):
    dists = computeNeighbors(target, targetdata, athletes)
    return sports[dists[0]]
def standardize(athletes, standards):
    for athlete in athletes:
        for stat in range(len(athletes[athlete])):
            athletes[athlete][stat] = (athletes[athlete][stat] - standards[stat][0])/standards[stat][1]
    return athletes
def stscore(vect):
    vect = sorted(vect)
    length = len(vect)
    if length%2!=0:
        median = (vect[length / 2] + vect[length / 2 - 1]) / 2.0
    else:
        median = vect[length / 2]
    stdev = sqrt(reduce(lambda x,y: x+y, [(x-median)**2 for x in vect])/length)
    return [median, stdev]
def unitTest():
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    assert(round(st, 3) == 65)
def test(trainingset, testset):
    with open(trainingset) as datafile:
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
        athletes=standardize(athletes, standards)
        with open(testset) as testdata:
            testreader = csv.reader(testdata, delimiter='	')
            testsports = {}
            testathletes = {}
            chars = []
            for i in range(len(testreader.next())-2):
                chars.append([])
            for row in testreader:
                for i in range(len(row)-2):
                    chars[i].append(int(row[i+2]))
                testsports[row[0]] = row[1]
                testathletes[row[0]] = [int(row[2]), int(row[3])]
            standards = map(stscore, chars)
            testathletes=standardize(testathletes, standards)
            correct = 0
            for athlete in testsports:
                prediction = classify(athlete, testathletes[athlete], athletes, sports)
                print(athlete+" - "+prediction)
                if(prediction==testsports[athlete]):
                    correct+=1
            print("Prediction acccuracy: "+str(correct*100.0/len(testsports))+"%")
test("athletesTestSet.txt", "athletesTrainingSet.txt")