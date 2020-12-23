import sys

def read_input(fname):
    with open(fname,'r') as f:
        depart = int(f.readline().rstrip())
        buses = [(i,int(x)) for i,x in enumerate(f.readline().rstrip().split(',')) if x != 'x']
    return (depart,buses)

def solve_part_1(depart,buses):

    distances = {}
    min_dist = float('inf')
    min_key = None
    for b in buses:        
        dist = b[1] * ((depart // b[1])+1) - depart
        if dist < min_dist:
            min_dist = dist 
            min_key = b[1]

    return min_key*min_dist

def solve_part_2(depart,buses):
    '''
     Find x such that x%d[0] = 0
                      x+offset(d[1],d[0])%d = 0
    '''    

    

depart_time,buses = read_input(sys.argv[1])
print("Ans:",solve_part_1(depart_time,buses))
# print("Ans part 2:",solve_p2(adapters))