def ways(order,currPrefList): # nmber of pref lists that start with this one and get to the order
    allCars = sorted(order)
    
    # check currPrefList
    for i,workingCar in enumerate(allCars[:len(currPrefList)]):
        finalSpot = order.index(workingCar)
        preferredSpot = ord(currPrefList[i])-65

        if finalSpot < preferredSpot: # Our car parked in a spot before its preference, can't happen!
            return 0

        for car in order[preferredSpot:finalSpot+1]:
            if car > workingCar: # This spot was empty but our car didn't take it, can't happen!
                return 0

    # Use the fundemental counting principle 
    prod = 1

    for workingCar in allCars[len(currPrefList):]:        
        finalSpot = order.index(workingCar)
        # opts = one it filled - firstAvailable + 1
        firstAvailable = finalSpot
        while firstAvailable >= 1:
            if order[firstAvailable-1] > workingCar: # the previous spot was empty, if our car wanted, it could have taken it
                break
            
            firstAvailable -= 1
        opts = finalSpot - firstAvailable + 1
        prod *= opts
    return prod

def solve(order,arn):
    allCars = sorted(order)
    ans = ""
    pos = 0
    while len(ans) < len(order):
        for let in allCars:
            let = let.upper()
            newAns = ans + let
            newPos = pos + ways(order,newAns)

            if newPos >= arn:
                ans = newAns
                break
            pos = newPos

    return ans

# 3(a)
order,arrangement = input().split(" ") #"cabd",5
arrangement = int(arrangement)
print(solve(order,arrangement))

## Random Test ##
# o = "cagfidhbe" # random test
# seen = set()

# prev = chr(60)
# for i in range(1,ways(o,"")):
#     x = solve(o,i)
#     assert prev < x
#     assert not x in seen
#     prev = x
#     seen.add(x)
