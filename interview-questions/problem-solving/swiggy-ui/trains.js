let arrival = [2, 2.1, 3, 3.2, 3.5, 5];
let departure = [2.3, 3.4, 3.2, 4.3, 4, 5.2];
 
function getMinPlatforms(arrival, departure) {
    const map = {};
    const minTime = Math.min(...arrival, ...departure);
    const maxTime = Math.max(...arrival, ...departure);
    // console.log('mintime is ', minTime, 'max time is ', maxTime);
    for (let i=minTime; i<=maxTime; i+=0.1) {
        i = Number(i.toFixed(1));
        // console.log('i is ',i);
        map[i] = 0;
    }
    // console.log(map);
    const numOfTrains = arrival.length;
    for (let i=0; i<numOfTrains; ++i) {
        let arrivalTime = arrival[i], departureTime = departure[i];
        for (let time = arrivalTime; time<=departureTime; time+=0.1) {
            time = Number(time.toFixed(1));
            map[time] += 1;
        }
    }
    console.log(map);
    // console.log(Object.values(map));
 
    return Math.max(...Object.values(map));
}
 
console.log(getMinPlatforms(arrival, departure));
 