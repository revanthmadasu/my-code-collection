const solution = (numbers) => {
    let largest = numbers[0] || 0;
    numbers.forEach(num => {
        if (num > largest) {
            largest = num;
        }
    });
    return largest;
};
