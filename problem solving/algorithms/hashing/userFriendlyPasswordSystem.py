'''
    tiktok assessment practice problem
    problem: https://www.hackerrank.com/test/14j0osksnmj/questions/85e6t96310l
    concepts: hashing, recursion, binary search
'''
import bisect
def f_hash(s):
    p = 131
    m = 10**9+7
    hash_value = 0
    n = len(s)
    for i in range(n):
        hash_value = (hash_value + ord(s[i]) * pow(p, len(s)-1-i, m)) % m
    p_hash_sum = (hash_value * p) % m
    return [hash_value, p_hash_sum]
def h(s, P=131, M=10**9+7):
    hash_value = 0
    for i, char in enumerate(s):
        hash_value = (hash_value + ord(char) * pow(P, len(s)-1-i, M)) % M
    return hash_value
def setPassword(s, act_hash_list, passwords_list):
    hashed_vals = f_hash(s)
    act_hash_list.append(hashed_vals[0])
    bisect.insort(passwords_list, hashed_vals[1])
    # passwords_dict[hashed_vals[0]] = True
    # passwords_dict[hashed_vals[1]] = True
    
def authEvents(events):
    passwords_list = []
    act_hash_list = []
    res = []
    for event in events:
        if event[0] == 'setPassword':
            passwords_list = []
            act_hash_list = []
            setPassword(event[1], act_hash_list, passwords_list)
        elif event[0] == 'authorize':
            hashed_val = int(event[1])
            if hashed_val in act_hash_list:
                res.append(1)
            else:
                closest = getClosestNum(passwords_list, hashed_val)
                if hashed_val >= closest and hashed_val <= (closest + 127):
                    res.append(1)
                else:
                    res.append(0)
                pass
            # res.append(1 if (hashed_val in passwords_dict or hashed_vals[1] in passwords_dict) else 0)
    return res
def getClosestNum(_list, target):
    n = len(_list)
    if n == 1:
        return _list[0]
    half_index = int(n/2)
    if _list[half_index] > target:
        return getClosestNum(_list[0:half_index], target)
    else:
        return getClosestNum(_list[half_index:], target)
test1 = [
    ["setPassword", "000A"],
    ["authorize", "108738450"],
    ["authorize", "108738449"],
    ["authorize", "244736787"]
]

test2 = [
    ["setPassword", "cAr1"],
    ["authorize", "223691457"],
    ["authorize", "303580761"],
    ["authorize", "100"],
    ["setPassword", "d"],
    ["authorize", "100"]
]

test3 = [
    ["setPassword", "1"],
    ["setPassword", "2"],
    ["setPassword", "3"],
    ["authorize", "49"],
    ["authorize", "50"],
]
# print(f_hash('cAr1'))
# print(f_hash('a'))
# print(f_hash('ab'))
# print(h('cAr1'))
# print(h('a'))
# print(h('ab'))

# print(authEvents(test1))
# print(authEvents(test2))
print(authEvents(test3))

print(getClosestNum([3,6,7,14,34,54],15))