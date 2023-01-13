function getMinimalTrips(arr) {

    let numsCount = {};

    // counting frequencies
    arr.forEach(num => {
        numsCount[num] = (numsCount[num] || 0) + 1;
    });

    let minTrips = 0;
    // console.log(numsCount);
    Object.values(numsCount).forEach(count => {

        if (count === 1) {
            // console.log("breaking");
            minTrips = -1;
        }
        if (minTrips !== -1) {
            minTrips += (Number.parseInt(count/3) + Number.parseInt((count%3)/2));
        }
    });
    return minTrips;
}

console.log(getMinimalTrips([2,4,6,6,4,2,4]));
console.log(getMinimalTrips([2,4,6,6,4,2,4,5]));
