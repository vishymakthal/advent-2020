import sys

def read_input(fname):
    arr = []
    with open(fname,'r') as f:
        ln = f.readline().rstrip()
        while(ln):
            arr.append(list(ln))
            ln = f.readline().rstrip()
    return arr

def in_bounds(row,col,max_row,max_col):

    return row >=0 and row < max_row and col >= 0 and col < max_col

def occupy_seat(layout,r,c):

    dirs = (
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (1,1),
        (-1,-1),
        (-1,1),
        (1,-1)
    )
    
    for d in dirs:
        row,col = (r+d[0],c+d[1])
        while(in_bounds(row,col,len(layout),len(layout[0])) and layout[row][col] == '.'):
            row,col = (row+d[0],col+d[1])
        if in_bounds(row,col,len(layout),len(layout[0])) and layout[row][col] == '#':
            return False
    
    return True 

def empty_seat(layout,r,c):
    
    dirs = (
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (1,1),
        (-1,-1),
        (-1,1),
        (1,-1)
    )

    cnt = 0
    for d in dirs:
        row,col = (r+d[0],c+d[1])
        while(in_bounds(row,col,len(layout),len(layout[0])) and layout[row][col] == '.'):
            row,col = (row+d[0],col+d[1])
        if in_bounds(row,col,len(layout),len(layout[0])) and layout[row][col] == '#':
            cnt += 1
    return cnt >= 5 

def execute_round(layout):
    diff = False
    to_be_taken = []
    to_be_emptied = []
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            if layout[r][c] == 'L':
                if occupy_seat(layout,r,c):
                    diff = True
                    to_be_taken.append((r,c))
            elif layout[r][c] == '#':
                if empty_seat(layout,r,c):
                    diff = True
                    to_be_emptied.append((r,c))
    for s in to_be_taken:
        layout[s[0]][s[1]] = '#'
    for s in to_be_emptied:
        layout[s[0]][s[1]] = 'L'

    
    return (layout,len(to_be_taken)+len(to_be_emptied))

def count_occupied(layout):

    cnt = 0
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            if layout[r][c] == '#':
                cnt += 1
    return cnt

def solve(layout):

    changed = 1 
    while(changed):
        
        layout,changed = execute_round(layout)

    return count_occupied(layout)


layout = read_input(sys.argv[1])
print("Ans:",solve(layout))
# print("Ans part 2:",solve_p2(adapters))