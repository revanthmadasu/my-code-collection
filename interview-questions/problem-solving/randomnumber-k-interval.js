/**
 * Asked in Swiggy interview
 * Generate random number in 0-N range with each generated number having k interval
 * For eg: if k is 10, then if 5 is generated for first time, it should be generated until next 10 generations
 */

// gives random method between given range
const getRandomNumber = (start, end) => {
    return Math.floor((end - start) * Math.random() + start);
}

// Linked List implementation of queue. 
/**
 * This is a modified implementation of queue
 * addElement will keep on adding util the queue is filled with k items, after k items on adding additional item it will append to end and remove the top element
 * @param {*} k max number of items queue can contain
 */
function Queue(k) {
    this.rootNode = undefined;
    this.lastNode = undefined;
    this.queueItems = {};
    this.maxLenght = k;
    this.queueLength = 0;
    this.addElement = function(item) {
        if (this.doesItemExists(item)) return;
        this.__insertIntoLinkedList__(item);
        if (this.queueLength > k) {
            const node = this.__removeFromTop__();
            delete this.queueItems[node.value];
            return node.value;
        }
    }
    this.doesItemExists = function(item) {
        return !!this.queueItems[item];
    }

    this.__insertIntoLinkedList__ = function (item) {
        if (!this.doesItemExists(item)) {
            const node = {
                value: item,
                next: null
            };
            if (this.lastNode) {
                this.lastNode.next = node;
                this.lastNode = node;
            } else {
                this.lastNode = node;
            }
            if (!this.rootNode) {
                this.rootNode = node;
            }
            this.queueItems[item] = true;
            this.queueLength += 1;
        }
    }

    this.__removeFromTop__ = function () {
        if (this.rootNode) {
            const node = this.rootNode;
            this.rootNode = node.next;
            this.queueLength -= 1;
            return node;
        }
    }
}

function main(n,k,numOfGenerations) {

    const queue = new Queue(k);
    const numbers = [];
    for (let i=1; i<= n; ++i) {
        numbers.push(i);
    }
    for (let i=0; i<numOfGenerations; ++i) {
        let randomIndex = getRandomNumber(0, numbers.length);
        let randomNumber = numbers[randomIndex];
        numbers[randomIndex] = numbers[numbers.length - 1];
        numbers.splice(numbers.length-1, 1);
        const addNumber = queue.addElement(randomNumber);
        if (addNumber) {
            numbers.push(addNumber);
        }
        console.log(i+'th number: ' + randomNumber);
    }
}

main(10,9,20);