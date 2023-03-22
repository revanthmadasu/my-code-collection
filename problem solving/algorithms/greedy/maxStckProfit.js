/**
 * concepts: arrays, greedy
 * asked in coding assessment
 */
/**
 * 
 * @param {number[]} prices 
 * @returns number
 */
const solution = (prices) => {
    /*
        Approach: calculating next max profit item. traversing array from last item. [prices.length - 1 - i] should get max profit item from i th element
        After generating nextMaxAry, parse prices array and difference between prices[i] and [prices.length - 1 - i] should give profit
        calculate profit for each price and select max profit
    */
    const nextMaxAry  = [];
    let max = prices[prices.length - 1];
    for (let i = prices.length - 1; i >= 0; --i) {
        if (max < prices[i]) {
            max = prices[i];
        }
        nextMaxAry.push(max);
    }
    let maxProfit = 0;
    prices.forEach((price, index) => {
        const nextMaxElement = nextMaxAry[prices.length - 1 - index];
        const profitGained = nextMaxElement - price;
        if (profitGained > maxProfit) {
            maxProfit = profitGained;
        }
    });
    return maxProfit;
};

