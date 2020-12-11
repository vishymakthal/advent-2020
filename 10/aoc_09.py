import sys

def read_input(fname):
    arr = []
    with open(fname,'r') as f:
        ln = f.readline().rstrip()
        while(ln):
            arr.append(int(ln))
            ln = f.readline().rstrip()
    return arr

def solve_p1(adapters):

    # go through the sorted ratings and note the diffs
    diffs = {}
    adapters.sort() 
    for i in range(1,len(adapters)):
        d = adapters[i] - adapters[i-1]
        diffs[d] = diffs.get(d,0) + 1
    return diffs[1]*diffs[3]

# without the cache this was actually not going to finish
cache = {}
def num_ways(ix,ratings):

    if ratings[ix] == None or ix < 0:
        return 0

    if cache.get(ix,False):
        return cache[ix]
    
    if ix == 0:
        cache[ix] = 1
        return 1

    ways = 0
    for i in range(1,4):
        ways += num_ways(ix-i, ratings) 

    cache[ix] = ways
    return ways

def solve_p2(adapters):
    ''' 
      1. sort the ratings
      2. make an array representing a number line with adapters marked
      3. cheeky recursion on the number line
      4. profit
    ''' 
    adapters.sort()
    ratings = [None for i in range(adapters[-1]+1)]
    for r in adapters:
        ratings[r] = r

    return num_ways(adapters[-1],ratings)

adapters = read_input(sys.argv[1])
adapters.append(0)
adapters.append(max(adapters)+3)
print("Ans part 1:",solve_p1(adapters))
print("Ans part 2:",solve_p2(adapters))