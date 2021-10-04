function reduce(reduceMethod) {
    console.log(`Revanth's reduce is being called on ${this}`);
    if (!this.length) {
        throw Error("No items are there to reduce");
    } else if (this.length === 1) {
        return this[0];
    } else {
        let accumulator = this[0];
        for(let i=0; i<this.length; ++i) {
            accumulator = reduceMethod(accumulator, this[i]);
        }
        return accumulator;
    }
}

Array.prototype.reduce = reduce;

const people2 = [
    {
        name: 'Revanth',
        age: 24
    },
    {
        name: 'Shravani',
        age: 24
    },
    {
        name: 'Rahul',
        age: 30
    }
];

const allPeopleNamesAggregated = people2.reduce((accumulated, current) => {
    return (accumulated.name ? accumulated.name : accumulated) + ', ' + current.name 
});

console.log('Reduced Value: ', allPeopleNamesAggregated);