const AutoMotive = {
    engineeringStream: 'Mechanical',
    hasEngine: true,
    getEngineeringStream: function() {
        return `Engineering stream of ${this.name} is ${this.engineeringStream}`
    }
};

const AutoMobile = {
    isMovable: true,
    canCarryPeople: true
};
AutoMobile.__proto__ = AutoMotive;

const Car = {
    numberOfWheels: 4,
    avgMaxSpeed: 150
}
Car.__proto__ = AutoMobile;

const BMW = {
    avgMaxSpeed: 200,
    name: "BMW",
}
BMW.__proto__ = Car;

console.log(BMW.getEngineeringStream());