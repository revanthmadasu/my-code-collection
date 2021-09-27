/**
 * get matched string index
 * found in hackerearth - adobe-coding-interview
 */
process.stdin.resume();
process.stdin.setEncoding('utf-8');

var input_ = "";

process.stdin.on('data', function (data) {
    input_ += data.toString().trim();
    input_ += '\n';
});

function Solve(Haycock, Needle) {
    const matchedIndex = Haycock.match(Needle);
    return Number(matchedIndex ? matchedIndex.index : -1);
}

process.stdin.on('end', function () {
    input_ = input_.replace(/\n$/, "");
    input_ = input_.split("\n");

    var [Haycock,Needle] = input_[0].split(' ');

    var out_ = Solve( Haycock,  Needle);
    process.stdout.write(out_.toString());

    process.exit();

});