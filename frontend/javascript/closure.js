function counter() {
    var counted = 0;
    return {
        incrementByOne: () => {
            counted++;
            return counted
        },
        incrementBy: (value) => {
            counted += value;
            return counted;
        },
        printedCounted: () => {
            console.log('Printing Counted', counted);
        }
    }
    // return function () {
    //     counted ++;
    //     return counted;
    // }
}

function Counter() {
    var counted = 0;
    this.incrementBy = function () {
        counted++;
        return counted
    }
    this.incrementByOne = function () {
        counted++;
        return counted
    }
    this.printedCounted = function() {
        console.log('Printing Counted', counted);
    }
}
var myCounter = counter()


console.log(myCounter.incrementByOne());
console.log(myCounter.incrementBy(10));
myCounter.printedCounted();

console.log('Counter2');

var myCounter2 = new Counter()

console.log(myCounter2.incrementByOne());
console.log(myCounter2.incrementBy(10));
myCounter2.printedCounted();
