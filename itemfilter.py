from pprint import pprint
from math import sqrt
def getSimilar(target, data, avgs):
	distances = {};
	for artist in data:
		if(artist!=target):
			distances[artist] = adjcosine(data[target], data[artist], avgs)
	pprint(distances);
def adjcosine(set1, set2, avgs):
	xy = 0
	x2 = 0
	y2 = 0
	for rater in set1:
		if rater in set2:
			xi = set1[rater]-avgs[rater]
			yi = set2[rater]-avgs[rater]
			xy+=xi*yi
			x2+=xi**2
			y2+=yi**2
	return (xy)/(sqrt(x2)*sqrt(y2));
def normalize(rating, dmin=1, dmax=5):
	normd = float(2*(rating-dmin)-(dmax-dmin))/float(dmax-dmin);
	return normd;
def denormalize(rating, dmin=1, dmax=5):
	denormd = dmin+(.5*(rating+1)*(dmax-dmin))
	return denormd;
users = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
"Lorde": 4, "Fall Out Boy": 1},
"Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
"Lorde": 4, "Fall Out Boy": 1},
"Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
"Lorde": 3, "Fall Out Boy": 1},
"Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
"Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
"Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
"Daft Punk": 5, "Fall Out Boy": 3}}
artists = {}
avgs = {}
for user in users:
	ratesum = 0;
	ratenum = 0;
	for artist in users[user]:
		ratenum+=1;
		ratesum+=users[user][artist];
		if artist not in artists:
			artists[artist] = {};
		artists[artist][user] = users[user][artist]
	avgs[user] = float(ratesum)/float(ratenum);
#pprint(artists)
#pprint(avgs)
#getSimilar('Lorde', artists, avgs) 
print(normalize(5.5, 1, 10))
