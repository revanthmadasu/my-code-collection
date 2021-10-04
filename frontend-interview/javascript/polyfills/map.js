function myMap(mappingFunction) {
    console.log('Revanth\'s map is being called on ' + this);
    const mappedArray = [];
    for(let i=0; i<this.length; ++i) {
        // mappedArray.push(mappingFunction(this[i]));
        mappedArray.push(mappingFunction(this[i]));
    }
    return mappedArray;
}
Array.prototype.map = myMap;

const people = [
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

console.log(people.map(person => person.name));