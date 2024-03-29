function myBind(bindingObject, ...args) {
    console.log(`Revanth's bind is being called`);
    const currentMethod = this;
    return function (...args) {
        return currentMethod.call(bindingObject, ...args);
    }
}

Function.prototype.mybind = myBind;

function sayMyName(prefix, sufix) {
    return `${prefix || ''}${this.name}${sufix || ''}`;
}

const singer = {
    name: 'Bebe Rexha'
};

const bindedSayMyName = sayMyName.mybind(singer);

console.log(sayMyName.call(singer));

console.log(bindedSayMyName('The one and only '));