'''Several algorithms are implemeted:
- If inflation is suspected (data is on different scales) use pearson
- If data is dense (not many non-zero values) use euclidian/manhattan
- If data is sparse use cosine
'''
import csv
from pprint import pprint
from math import sqrt
def getRecomendation(target, data, algorithm, k):
	targetdata = data[target]
	distances = {};
	for user in data:
		if(user != target):
			distances[user] = algorithm(targetdata, data[user])
	closestnames  = sorted(distances, key=distances.get)
	#pprint(distances);
	if algorithm==pearson:
		print("Closest user was: "+closestnames[0]+" with a coefficient of: "+str(-distances[closestnames[0]]));
	else:	
		print("Closest user was: "+closestnames[0]+" with a distance of: "+str(distances[closestnames[0]]));
	recmovies = [];
	n = k
	for i in range(0, k-1):
		for movie in data[closestnames[i]]:
			if (movie not in data[target]) and (movie not in recmovies):
				print(movie+" - "+data[closestnames[i]][movie]);
				recmovies.append(movie);
	while recmovies == [] and n<k+3:
		for movie in data[closestnames[i]]:
			if (movie not in data[target]) and (movie not in recmovies):
				print(movie+" - "+data[closestnames[i]][movie]);
				recmovies.append(movie);
		n+=1;
	if recmovies == []:
		print("Could not find any recomendations");
def getMovies(target, relation):
	for movie in relation:
		if movie in target:
			pass;
		else:
			print(movie);
def manhattan(set1, set2):
	dist = 0;
	for movie in set1:
		if movie in set2:
			dist = dist+abs(float(set1[movie])-float(set2[movie]))
	return dist;
def euclidian(set1, set2):
	dist = 0;
	for movie in set1:
		if movie in set2:
			dist = dist+(float(set1[movie])-float(set2[movie]))**2
	return sqrt(dist);
def cosine(set1, set2):
	dist = 0;
	vectorx = 0;
	vectory = 0;
	xy = 0;
	for movie in set1:
		if movie in set2:
			vectorx = vectorx + float(set1[movie])**2
			vectory = vectory + float(set2[movie])**2
			xy = xy + (float(set1[movie])*float(set2[movie]))
	vectorx = sqrt(vectorx)
	vectory = sqrt(vectory)
	return xy/(vectorx*vectory);
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
			xi = float(set1[movie]);
			yi = float(set2[movie]);
			xy = xy +(xi*yi);
			x = x + xi;
			y = y + yi;
			x2 = x2 + xi**2
			y2 = y2 + yi**2
	numer = xy-((x*y)/n);
	denom = sqrt(x2-(x**2/n))*sqrt(y2-(y**2/n));
	try:
		return -numer/denom;
	except:
		return 1
movies = {}
users = {}
emptys = 0; #Counter for empty ratings to determine data density
total = 0;
with open("Movie_Ratings.csv") as datafile:
	reader = csv.DictReader(datafile)
	addzeros = 0;
	for row in reader:
		moviename = row.pop('');
		movies[moviename] = row;
		for user in row:
			total+=1;
			if(row[user]== '' and addzeros == 1):
				row[user] = 0;
				emptys+=1
			if(row[user]!=''):
				if (user in users):
					users[user][moviename] = row[user];
				else:
					users[user] = {};
					users[user][moviename] = row[user];
			else:
				emptys +=1;			 
	#pprint(users);
	density = (float(total-emptys)/float(total));
	if(density>.75):
		alg = euclidian
	else:
		alg = cosine
	#pprint(movies);
	getRecomendation("jim", users, alg, 3)
	'''for targetname in users:
		print("For user "+targetname);
		getRecomendation(targetname, users, manhattan, 2)
		getRecomendation(targetname, users, euclidian, 2)
		getRecomendation(targetname, users, pearson, 2)'''
