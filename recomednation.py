import csv
from pprint import pprint
from math import sqrt
def getRecomend(user, data, algorithm):
	for moviename in data:
		movie = data[moviename]
		if movie[user]:
			print(moviename+" - "+movie[user])
movies = {}
users{}
with open("Movie_Ratings.csv") as datafile:
    reader = csv.DictReader(datafile)
    for row in reader:
		name = row.pop('');
		movies[name] = row;
		pprint(row)
    #pprint(movies);
    #getRecomend("brian", movies, "tes")
	
