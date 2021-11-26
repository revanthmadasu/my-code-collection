let nums = [10,12,10,15,-1,7,6,5,4,2,1,1,1]
let target = 11;
 
function targetSum(nums, target) {
    const map = {};
    nums.forEach(element => {
        if (!map[element]) {
            map[element] = 1;
        } else {
            map[element] += 1;
        }
    });
    const result = [];
    console.log(map);
    nums.forEach(element => {
        // console.log()
        if ((map[element] && map[target-element]) && (target-element === element ? map[target-element] > 1: true)) {
            result.push([element, target-element]);
            map[target-element] -= 1;
            map[element] -= 1;
        }
    });
    return result;
}
 
console.log(targetSum(nums, target));
console.log(targetSum(nums, target).length);
 

