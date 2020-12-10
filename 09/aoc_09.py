import sys


def read_input(fname):
    seq = []
    with open(fname,'r') as f:

        ln = f.readline().rstrip()
        while(ln):
            seq.append(int(ln))
            ln = f.readline().rstrip()
    return seq

def two_sum(seq,left,right):

    target = seq[right]
    seek = {}
    for i in range(left,right):
        if seq[i] in seek:
            return True
        seek[target-seq[i]] = seq[i]

    return False

def solve_p1(seq, buf_len):
    
    for i in range(buf_len,len(seq)):
        if not two_sum(seq,i-buf_len-1,i): 
            return seq[i]

def solve_p2(buf,target):

    left = right = 0
    s = buf[left] 
    while s != target:
        
        if s > target:
            left += 1
            right = left
        if s < target:
            right += 1 
        s = sum(buf[left:right+1])
    return min(seq[left:right+1]) + max(seq[left:right+1])


seq = read_input(sys.argv[1])
p1 = solve_p1(seq,int(sys.argv[2]))
print("Ans part 1:", p1)

p2 = solve_p2(seq,p1)
print("Ans part 2:", p2)