'''
    tiktok practice problem - distinct target sum pairs
    problem: https://www.hackerrank.com/test/14j0osksnmj/questions/521e9583119db
    concepts: arrays, hashmap
'''
def stockPairs(stocksProfit, target):
    print(stocksProfit, target)
    stocksDict = dict()
    for profit in stocksProfit:
        stocksDict[profit] = True
    uniqueStocks = stocksDict.keys()
    res = set()
    for stock in uniqueStocks:
        if (target - stock) in stocksDict:
            l = [stock, target - stock]
            res.add((min(l), max(l)))
    print(res)
    return len(res)

print(stockPairs([6, 6, 3, 9, 3, 5, 1], 12))