from collections import defaultdict

nodesMap = defaultdict(lambda: None)

nodesMap['a'] = ['b','c','d','e']

nodesMap['b'] = ['d']
nodesMap['a'] = ['b','c','d','e']
nodesMap['a'] = ['b','c','d','e']
nodesMap['a'] = ['b','c','d','e']
queue = ['a']

while len(queue):
    item = queue.pop(0)
    nextItems = nodesMap[item]
    queue.extend(nextItems)
    print(item)
    checkForItemsInQueue(queue, nextItems)

def checkForItemsInQueue(queue, nextItems):
    remove = []
    for item in queue:
        if item in nextItems:
            remove.append(nextItems.remove(item))
    