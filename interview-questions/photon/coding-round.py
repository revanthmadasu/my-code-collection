
# Online Python - IDE, Editor, Compiler, Interpreter

'''
aaaahhhhiiikkkeeelllaaa
a4h4i3k3e3l3a3
'''

def encodeTo(s):
    res = ''
    i = 0
    while i < len(s):
        curCh = s[i]
        j = i
        while j < len(s) and s[j] == curCh:
            j += 1
        res += (curCh + str(j-i))
        i = j
    return res
print(encodeTo('aaaahhhhiiikkkeeelllaaa'))

'''
[1,5,6,9,10]
[2,3,4,7,8,11,12,13,14,15]
'''
def mergeSortedLists(list1, list2):
    resList = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            resList.append(list1[0])
            list1.pop(0)
        else:
            resList.append(list2[0])
            list2.pop(0)
    if len(list1):
        resList.extend(list1)
        # print(f'b1 {resList}')
    if len(list2):
        resList.extend(list2)
        # print(f'b2 {resList}')
    return resList
print(mergeSortedLists([1,5,6,9,10], [2,3,4,7,8,11,12,13,14,15]))

'''
Input: A= [-7, 1, 5, 2, -4, 3, 0]
Output: 3
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
 
Input: A= [7, 1, 5, 2]
Output: 1
3 is an equilibrium index, because:
A[0] =A[3] + A[2]
'''

def getEquilibriumIndex(arr):
    prefixSum = []
    _sum = 0
    for num in arr:
        _sum += num
        prefixSum.append(_sum)
    for i in range(len(arr)):
        leftSum = prefixSum[i-1] if i-1 >= 0 else 0
        rightSum = prefixSum[-1] - prefixSum[i]
        if leftSum == rightSum:
            return i
    return -1
print(getEquilibriumIndex([-7, 1, 5, 2, -4, 3, 0]))
print(getEquilibriumIndex([7, 1, 5, 2]))
print(getEquilibriumIndex([1, 2, 3, 4]))
