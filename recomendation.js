/*Several algorithms will be implemeted:
- If inflation is suspected (data is on different scales) use pearson
- If data is dense (not many non-zero values) use euclidian/manhattan
- If data is sparse use cosine
*/
var fs = require("fs");
var parse = require("csv-parse");
var sqrt = Math.sqrt
var datafile = "Movie_Ratings.csv";
var parser = parse({delimiter: ',', colums: true}, function(err, data){
    if(err){
        console.log(err);
    }
    else{
        console.log(data);
    }
});
fs.createReadStream(datafile).pipe(parser);