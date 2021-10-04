sum(10)(20)(30)(40)(100);

var total;
function sum (val) {
    let total = val;
    function addToArr (nextVal) {
        total += nextVal;
        // console.log(ary.reduce((a,b) => a+b));
        console.log(total);
        return addToArr;
    }
    return addToArr;
}

