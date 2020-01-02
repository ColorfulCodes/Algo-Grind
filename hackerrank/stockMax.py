def stockmax(prices):
    maxGain = 0
    while len(prices)>0:
        maxIndex = prices.index(max(prices))
        maxNum = max(prices)
        maxGain +=sum([maxNum-i for i in prices[:maxIndex]])
        prices = prices[maxIndex+1:]

    return maxGain
    
print(stockmax([1,3,1,2]))