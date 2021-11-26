function factorial() {
    const memorized = {1:1};
    let lastCalculated = 1;
    return function inner_impl(n) {
        console.log('n is ',n);
        if (memorized[n]) {
            return memorized[n];
        }
        let num= n;
        while(num>0) {
            if (memorized[num]){
                break;
            }
            --num;
        }
        let factorial = memorized[num] || 1;
        console.log(memorized);
        for (let i=num+1; i<=n; ++i) {
            console.log('called');
            factorial*=i;
            memorized[i] = factorial;
        }
        lastCalculated = Math.max(n,lastCalculated);
        return factorial;
    }
}
 
const myFactorial = factorial();
// console.log(factorial(4));
console.log(myFactorial(5));
console.log(myFactorial(4));
console.log(myFactorial(10));
 
