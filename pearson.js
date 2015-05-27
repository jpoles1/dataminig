pearson = function(x, y){
    len = x.length;
    sumx = sum(x);
    sumy = sum(y);
    sumxy = multsum(x,y);
    numer = sumxy-((sumx*sumy)/len);
    denom = Math.sqrt(sqrsum(x)-(sumx*sumx/len))*Math.sqrt(sqrsum(y)-(sumy*sumy/len));
    return numer/denom;
}
sum = function(set){
    var sum=0;
    for (var i=0,n=set.length; i<n; i++) {
      sum+=set[i];
    }
    return sum;
}
multsum = function(x,y){
    var sum=0;
    for (var i=0,n=x.length; i<n; i++) {
      sum+=x[i]*y[i];
    }
    return sum;
}
sqrsum = function(set){
    var sum=0;
    for (var i=0,n=set.length; i<n; i++) {
      sum+=Math.pow(set[i],2);
    }
    return sum;
}
set1 = [4.75, 4.5, 5, 4.25,4];
set2 = [4, 3, 5, 2, 1];
console.log(pearson(set1, set2));
