
def get_id(ec):

    i = left = 0
    right = 127
    
    while(i < 7):

        mid = left + (right - left)//2
        if ec[i] == 'F':
            right = mid
        else:
            left = mid

        i += 1

    row = right

    i = 7
    left = 0
    right = 7
    while(i < len(ec)):
        
        mid = left + (right - left)//2
        if ec[i] == 'L':
            right =  mid
        else:
            left = mid

        i += 1
    col = right


    return row * 8 + col

max_val = float('-inf')
min_val = float('inf')
su = 0
with open('in.txt','r') as f:
        ln = f.readline().rstrip()
        while(ln):
            _id = get_id(ln)
            max_val = max(max_val, int(_id))
            min_val = min(min_val, int(_id))
            su += int(_id)
            ln = f.readline().rstrip()

print(min_val,max_val)
t = sum(range(8,977))
print(t-su)

