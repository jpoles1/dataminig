manhattan = function(ax, ay, bx, by){
	dist = Math.abs(ax-bx)+Math.abs(ay-by);
	return dist;
}
euclidian = function(ax, ay, bx, by){
    dist = Math.sqrt(Math.pow((ax-bx),2)+Math.pow((ay-by),2));
    console.log(dist);
    return dist;
}
users = ["amy", "bill", "jim"];
movies = {"snowcrash": {"amy": 5, "bill": 2 , "jim": 1}, "girl": {"amy": 5, "bill": 5, "jim": 4}};
close = 100
closename = "";
for(i = 0; i < users.length; i++){
    snowcrash = movies.snowcrash[users[i]];
    girl = movies.girl[users[i]];
    res = euclidian(4,2,snowcrash,girl);
    if(res<close){
        close = res;
        closename = users[i];
    }
}
if(closename == ""){
    console.log("Failed to find a close match");
}
else{
    console.log("Matched with: "+closename+" with a distance of: "+close);
}
