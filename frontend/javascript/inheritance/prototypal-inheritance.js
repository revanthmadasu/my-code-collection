function Human() {
    this.species = 'Homosapiens';
    this.noOfLimbs = 4;
    this.describe = function () {
        const description = `${this.name ? 'Hi, I am ' + this.name + '.': ''} I communicate by ${this.communicate()}. Also my other modes of communication are ${this.modeOfCommunication}. ${this.whatCanDo ? 'What I can do is I ' + this.whatCanDo : ''}`;
        console.log(description);
        return description;
    }
}

function Infant(name) {
    this.name = name || '';
    this.communicate = function () {
        return "cries - waah";
    };
    this.modeOfCommunication = ['Cry', 'Laugh', 'Facial Expression'];
}
Infant.prototype = new Human();

function Adult(name) {
    this.name = name || '';
    this.communicate = function () {
        return "talks - blah blah blah";
    }
    this.modeOfCommunication = ['Talk', 'Insult', 'Cry', 'Laugh', 'Facial Expression'];
}
Adult.prototype = new Human();

function Doctor(name) {
    this.name = name || '';
    this.whatCanDo = "Treat people and make them better";
}
Doctor.prototype = new Adult();

function Engineer(name) {
    this.name = name || '';
    this.whatCanDo = "Build world and make it better place (or even worse if it goes wrong)";
}
Engineer.prototype = new Adult();



const harini = new Doctor('Harini');
harini.describe();

const revanth = Object.create(new Engineer('Revanth'))
revanth.describe();

const roshan = new Infant('Roshan');
roshan.describe();