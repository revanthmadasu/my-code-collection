function MergeSort(arr) {
    return divide(arr);
}

function divide(arr) {
    if (arr.length === 1) {
        return arr;
    } else {
        const mid = Math.ceil(arr.length/2);
        let arr1 = arr.slice(0,mid);
        let arr2 = arr.slice(mid, arr.length);
        const sortedArr1 = divide(arr1);
        const sortedArr2 = divide(arr2);
        const sortedArr = merge(sortedArr1, sortedArr2);
        return sortedArr;
    }
}

function merge(arr1, arr2) {
    let num1 = arr1[0];
    let num2 = arr2[0];
    let i1 = 0, i2 = 0;
    let arr2Parsed = false, arr1Parsed = false;
    const sortedArr = [];
    while (i1 < arr1.length || i2 < arr2.length) {
        if (i1 == arr1.length) {
            arr1Parsed = true;
        }
        if (i2 == arr2.length) {
            arr2Parsed = true;
        }
        num1 = arr1[i1];
        num2 = arr2[i2];
        if ((arr2Parsed) || (num1 < num2)) {
            sortedArr.push(num1);
            ++i1;
        } else if ((arr1Parsed) || (num1 >= num2)){
            sortedArr.push(num2);
            ++i2;
        }
    }
    console.log('out of loop');
    return sortedArr;
}

const arr = [10,30,4,3,40,32,10,33];
console.log(`merged : ${MergeSort(arr)}`);