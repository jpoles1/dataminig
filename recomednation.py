import csv
from pprint import pprint
from math import sqrt
def getRecomend(target, data, algorithm):
	targetdata = data[target]
	closest = 0;
	closestname = "";
	for user in data:
		if(user != target):
			dist = algorithm(targetdata, data[user])
			if dist < closest or closest == 0:
				closest = dist;
				closestname = user;
	print("Closest user was: "+closestname+" with a distance of: "+str(closest));
def manhattan(set1, set2):
	dist = 0;
	for movie in set1:
		if movie in set2:
			dist = dist+abs(int(set1[movie])-int(set2[movie]))
	return dist;
def euclidian(set1, set2):
	dist = 0;
	for movie in set1:
		if movie in set2:
			dist = dist+(int(set1[movie])-int(set2[movie]))**2
	return sqrt(dist);
def pearson(set1, set2):
	n = 0;
	dist = 0;
	xy = 0;
	x = 0;
	y = 0;
	x2 = 0;
	y2 = 0;
	for movie in set1:
		if movie in set2:
			n = n + 1;
			xi = int(set1[movie]);
			yi = int(set2[movie]);
			xy = xy +(xi*yi);
			x = x + xi;
			y = y + yi;
			x2 = x2 + xi**2
			y2 = y2 + yi**2
	numer = xy-((x*y)/n);
	denom = sqrt(x2-(x**2/n))*sqrt(y2-(y**2/n));
	return numer/denom;
movies = {}
users = {}
with open("Movie_Ratings.csv") as datafile:
	reader = csv.DictReader(datafile)
	for row in reader:
		moviename = row.pop('');
		movies[moviename] = row;
		for user in row:
			if(row[user]!=''):
				if (user in users):
					users[user][moviename] = row[user];
				else:
					users[user] = {};
					users[user][moviename] = row[user];
	#pprint(users);
	#pprint(movies);
	targetname = "greg";
	getRecomend(targetname, users, manhattan)
	getRecomend(targetname, users, euclidian)
	getRecomend(targetname, users, pearson)
