def get_inputs():
    print()
    # m rows, n columns
    m,n = list(map(int, input("Enter grid dimentions -inp format: csv\n").split(",")))
    nodes = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(j + (i*n))
        nodes.append(col)

    blockedNodes = list(map(int, input("Enter blocked nodes  -inp format: csv\n").split(",")))
    
    noOfPirates = int(input("Enter number of pirates\n"))
    pirateCycles = []
    for i in range(noOfPirates):
        pirateCycles.append(list(map(int, input(f"Enter pirate cycle for {i+1}th pirate - inp format: csv. Eg: 1,2,3,1\n").split(","))))

    startingPoint, endingPoint = list(map(int, input("Enter starting and destination points -inp format: csv\n").split(",")))
    return [m, n, nodes, blockedNodes, pirateCycles, startingPoint, endingPoint]

def get_neighbours(currentNode, blockedNodes, nodes):
    noOfCols = len(nodes[0])
    noOfRows = len(nodes)
    currentRow = int(currentNode/noOfCols)
    currentCol = currentNode%noOfCols
    neighbours = []
    def add_node(node):
        if not node in blockedNodes:
            neighbours.append(node)
    if currentCol - 1 >= 0:
        add_node(nodes[currentRow][currentCol-1])
    if currentCol + 1 < noOfCols:
        add_node(nodes[currentRow][currentCol+1])
    if currentRow - 1 >= 0:
        add_node(nodes[currentRow - 1][currentCol])
    if currentRow + 1 < noOfRows:
        add_node(nodes[currentRow + 1][currentCol])
    return neighbours

def conflict_occurs(node, parentNode, currentStep, pirateCycles):
    for pirateCycle in pirateCycles:
        cycleLength = len(pirateCycle)
        if pirateCycle[currentStep%cycleLength] == node:
            return True
        if pirateCycle[currentStep%cycleLength] == parentNode and pirateCycle[(currentStep-1)%cycleLength] == node:
            return True
    return False

def bfsTraversal(nodes, blockedNodes, pirateCycles, startingPoint, endingPoint):
    def get_stack_node(node, parentNode, path):
        stack_node = dict()
        stack_node['val'] = node
        stack_node['parentNode'] = parentNode
        stack_node['path'] = path
        return stack_node

    # stack = [get_stack_node(neighbour, startingPoint, f"{startingPoint}-")
    #          for neighbour in get_neighbours(startingPoint, blockedNodes, nodes)]
    stack = [get_stack_node(startingPoint, -1, f"{startingPoint}-")]
    currentStep = 1
    while(True):
        newStack = []
        newNodesStack = []
        def append_to_stack(nodeItem):
            if not nodeItem['val'] in newNodesStack:
                newNodesStack.append(nodeItem['val'])
                newStack.append(nodeItem)
        for nodeObj in stack:
            node = nodeObj.get('val')
            neighbours = get_neighbours(node, blockedNodes, nodes)
            for neighbour in neighbours:
                if not conflict_occurs(neighbour,node,currentStep, pirateCycles):
                    if neighbour==endingPoint:
                        return f"{nodeObj.get('path')}{neighbour}"
                    append_to_stack(get_stack_node(neighbour, node, f"{nodeObj.get('path')}{neighbour}-"))
        stack=newStack
        currentStep += 1
        if len(stack) == 0:
            return "no answer"
        

def main():
    m, n, nodes, blockedNodes, pirateCycles, startingPoint, endingPoint = get_inputs()
    print(bfsTraversal(nodes, blockedNodes, pirateCycles, startingPoint, endingPoint))

    # print(m, n, nodes, blockedNodes, pirateCycles, startingPoint, endingPoint)
    # print(bfsTraversal([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [10], [[0, 4, 5, 1, 0], [5, 9, 10, 11, 7, 3, 7, 11, 10, 9, 5, 1, 5], [9, 10, 6, 5, 9], [2, 6, 10, 9, 8, 4, 0, 1, 2], [11, 7, 6, 10, 11]], 7, 4))
    # print(get_neighbours(11,[2, 10],[[0,1,2,3],[4,5,6,7],[8,9,10,11]]))

main()