def ways(order,currPrefList): # number of pref lists that start with this one and get to the order
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

# 3 (b)
# Simple simulation. 

# 3 (c)
# If there are only two possible preference lists then given such arrangement one car has two possible
# preferences, and all the rest parked in their preffered spots.
#
# Note that the preferred spot of a car will always be equal to, or to the left of its final spot.
# So if the car on our left came after us, we are in our preffered spot.
#
# The car with two possible preffered spots must be directly to the right of a car came before it.
# If this car is 'a' then we have 0 possible arrangements. ('a' always gets its preference)
# If it is 'b' then we have 1 possible arrangement. (pon..cab)
# If it is 'c' then we have 2 possible arrangements. (pon..dacb, pon..dbca)
# ...
# If it is 'p' then we have 15 possible arrangements. 
#
# The total number of arrangements is 0 + 1 + ... + 15 = 120

# 3 (d)

# Note that car 'a' is always in its preferred position
# Note a car's preffered position is always <= (left of or exactly) its final position.
# Therefore, if a car is not in its preffered position then it's preffered position is < (left of) its final position
# We use this information, and the fundemental counting principle, to count the total number of possible pref lists.


from itertools import combinations
CARS = "abcdefghijklmnop"

possHappyCars = [('a',) + cs for cs in combinations(CARS[1:],2)] 

s = 0
for happyCars in possHappyCars:
    otherCars = set(CARS) - set(happyCars)
    p = 1
    for sadCar in otherCars:
        p *= ord(sadCar) - ord('a')
    s += p

print(f"{s:,}")

# This computation gives us the answer 6,165,817,614,720