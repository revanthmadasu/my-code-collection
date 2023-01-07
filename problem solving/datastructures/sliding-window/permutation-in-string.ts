/**
 *  https://leetcode.com/problems/permutation-in-string
 *  Concepts: Sliding Window, Hash Table, Two Pointers, String 
 */
function checkInclusion(s1: string, s2: string): boolean {
    let s1CharCount = {};
    s1.split('').forEach(ch => {
        s1CharCount[ch] = (s1CharCount[ch] || 0) + 1;
    });
    let hashLastIndex = s2.length - s1.length;
    let hashTables = {};
    let result = false;
    const addAndCheck = (table, ch) => {
        table.s1Count += 1;
        table.s1CharCount[ch] -= 1;
        if (table.s1Count === s1.length) {
            result = true;
            return true;
        }
        return false;
    }
    for(let i=0; i<s2.length; ++i) {
        let ch = s2[i];
        const tablesToRemove: any[] = [];
        for (let index in hashTables) {
            let table = hashTables[index];
            if (table.s1CharCount[ch]) {
                if (addAndCheck(table, ch)) {
                    break;
                }
            } else {
                tablesToRemove.push(table.index);
            }
        }
        if (result) {
            break;
        }
        if (s1CharCount[ch] && i<=hashLastIndex){
            const table = {
                index: i,
                s1Count: 0,
                s1CharCount: { ...s1CharCount }
            };
            hashTables[i] = table;
            if (addAndCheck(table, ch)) {
                break;
            }
        }
        tablesToRemove.forEach(index => delete hashTables[index]);
    }
    return result;
};