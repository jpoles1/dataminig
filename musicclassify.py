cats = "piano, vocals, beat, blues, guitar, backup vocals, rap".split(", ")
items = {"Dr Dog/Fate": [2.5, 4, 3.5, 3, 5, 4, 1],
 "Phoenix/Lisztomania": [2, 5, 5, 3, 2, 1, 1],
 "Heartless Bastards/Out at Sea": [1, 5, 4, 2, 4, 1, 1],
 "Todd Snider/Don't Tempt Me": [4, 5, 4, 4, 1, 5, 1],
 "The Black Keys/Magic Potion": [1, 4, 5, 3.5, 5, 1, 1],
 "Glee Cast/Jessie's Girl": [1, 5, 3.5, 3, 4, 5, 1],
 "La Roux/Bulletproof": [5, 5, 4, 2, 1, 1, 1],
 "Mike Posner": [2.5, 4, 4, 1, 1, 1, 1],
 "Black Eyed Peas/Rock That Body": [2, 5, 5, 1, 2, 2, 4],
 "Lady Gaga/Alejandro": [1, 5, 3, 2, 1, 2, 1],
 "Cagle": [1, 5, 2.5, 1, 1, 5, 1]}
users = {"Angelica": {"Dr Dog/Fate": "L", "Phoenix/Lisztomania": "L",
 "Heartless Bastards/Out at Sea": "D",
"Todd Snider/Don't Tempt Me": "D",
"The Black Keys/Magic Potion": "D",
"Glee Cast/Jessie's Girl": "L",
"La Roux/Bulletproof": "D",
"Mike Posner": "D",
"Black Eyed Peas/Rock That Body": "D",
"Lady Gaga/Alejandro": "L"},
 "Bill": {"Dr Dog/Fate": "L", "Phoenix/Lisztomania": "L",
 "Heartless Bastards/Out at Sea": "L",
"Todd Snider/Don't Tempt Me": "D",
"The Black Keys/Magic Potion": "L",
"Glee Cast/Jessie's Girl": "D",
"La Roux/Bulletproof": "D", "Mike Posner": "D",
 "Black Eyed Peas/Rock That Body": "D",
"Lady Gaga/Alejandro": "D"} }
def manhattan(v1, v2):
    dist = 0;
    if(len(v1)==len(v2)):
        for i in range(len(v1)):
           dist+=abs(v1[i]-v2[i])
        return dist
    else:
        raise ValueError("Vectors not the same length")
def computeNeighbors(target, songs):
    dists = {}
    for song in songs:
        if(song!=target):
            dists[song] = manhattan(songs[target], songs[song])
    return sorted(dists, key=dists.get)
def classify(target, user, songs, users):
    dists = computeNeighbors(target, songs)
    print dists
    return users[user][dists[0]]
print(classify("Cagle", "Angelica", items, users))