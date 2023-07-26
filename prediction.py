import math, copy

def showOutstanding(vector):
    print("Current Outstanding Shares: %f & %f"  % (vector[0], vector[1]))

def showProbablity(vector):
    print("Current Probablity Of Wining: %f & %f"  % (vector[0], vector[1]))

def probablities(outstanding, liq):
    result = []
    for i in range(len(outstanding)):
        result.append(0)
    
    denom = 0

    for i in range(len(outstanding)):
        denom += math.exp(outstanding[i] / liq)

    for i in range(len(outstanding)):
        result[i] = math.exp(outstanding[i] / liq) / denom

    return result

def cost(outstanding, liq):
    sum = 0
    for i in range(len(outstanding)):
        sum += math.exp(outstanding[i] / liq)

    print("Sum: ", sum)
    calc = liq * math.log(sum)
    print("Calc: ", calc)
    return calc

def costOfTrans(outstanding, idx, nshares, liq):
    after = copy.copy(outstanding)
    print("After [before]: ", after)
    after[idx] += nshares
    print("After [after]: ", after)
    print("Outstanding: ", outstanding)
    newcost =  cost(after, liq) - cost(outstanding, liq)
    print("New Cost: ", newcost)
    return newcost

def costForOneShare(outstanding, liq):
    result = [0 ,0]

    result[0] = costOfTrans(outstanding, 0, 1, liq)
    result[1] = costOfTrans(outstanding, 1, 1, liq)

    return result



liquidity = 100
print("Liquidity is: ", liquidity)
outstanding = [0, 0] #new vector to store outstanding shares
showOutstanding(outstanding)
prob = probablities(outstanding, liquidity)
showProbablity(prob)

print("=================================")

print("If Expert buys 20 shares of A")

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)

costTrans = costOfTrans(outstanding, 0, 20, liquidity)
print("Cost of transaction to expert: ", costTrans)

outstanding = [20, 0]
showOutstanding(outstanding)

prob = probablities(outstanding, liquidity)
showProbablity(prob)

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)


print("=================================")

print("If Expert buys 20 shares of B")

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)

costTrans = costOfTrans(outstanding, 0, 20, liquidity)
print("Cost of transaction to expert: ", costTrans)

outstanding = [20, 20]
showOutstanding(outstanding)

prob = probablities(outstanding, liquidity)
showProbablity(prob)

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)


print("=================================")

print("If Expert sell 10 shares of A")

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)

costTrans = costOfTrans(outstanding, 0, 20, liquidity)
print("Cost of transaction to expert: ", costTrans)

outstanding = [10, 20]
showOutstanding(outstanding)

prob = probablities(outstanding, liquidity)
showProbablity(prob)

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)

print("=================================")

print("If Expert buys 100 shares of B")

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)

costTrans = costOfTrans(outstanding, 0, 20, liquidity)
print("Cost of transaction to expert: ", costTrans)

outstanding = [0, 1200]
showOutstanding(outstanding)

prob = probablities(outstanding, liquidity)
showProbablity(prob)

costPerShare = costForOneShare(outstanding, liquidity)
print("Cost for one share: ", costPerShare)
