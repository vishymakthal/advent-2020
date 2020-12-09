import sys


def get_instructions(fname):
    
    inst = []

    with open(fname,'r') as f:
        ln = f.readline()

        while(ln):

            op,offset = ln.rstrip().split(' ')
            inst.append([op,int(offset)]) 
            ln = f.readline()

    return inst

def get_nops_and_jmps(inst):

    ixs = []

    for i,v in enumerate(inst):
        if v[0] == 'jmp' or v[0] == 'nop':
            ixs.append(i)

    return ixs

def solve_p1(fname):

    inst = get_instructions(fname)
    acc = 0

    with open(fname,'r') as f:
        ln = f.readline()

        while(ln):

            op,offset = ln.rstrip().split(' ')
            inst.append((op,int(offset))) 
            ln = f.readline()

    executed = set()    
    i = 0
    while(i not in executed):

        executed.add(i)
        op,offset = inst[i]
        
        if op == 'acc':
            acc += offset
            i += 1
        if op == 'jmp':
            i += offset
        if op == 'nop':
            i += 1
        
    return acc

# BRUTE FORCE DA TING
def solve_p2(fname):

    inst = get_instructions(fname)
    for ix in get_nops_and_jmps(inst):
        if inst[ix][0] == 'jmp':
            inst[ix][0] = 'nop'
        elif inst[ix][0] == 'nop':
            inst[ix][0] = 'jmp'
        
        acc = 0
        i = 0
        executed = set()
        while((i not in executed) and (i < len(inst))):
            executed.add(i)
            op,offset = inst[i]
            
            if op == 'acc':
                acc += offset
                i += 1
            if op == 'jmp':
                i += offset
            if op == 'nop':
                i += 1

        if i in executed:
            if inst[ix][0] == 'jmp':
                inst[ix][0] = 'nop'
            elif inst[ix][0] == 'nop':
                inst[ix][0] = 'jmp'
        elif i >= len(inst):
            return acc

# print(solve_p1(sys.argv[1]))
print(solve_p2(sys.argv[1]))