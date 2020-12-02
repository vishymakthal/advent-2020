
valid = 0 
valid2 = 0

def validate(char,string,upper,lower):

    cnt = 0
    for c in string:
        if c == char:
            cnt += 1
        
        if cnt > upper:
            return False
    
    return cnt >= lower
            
def validate_v2(char,string,u_ix,l_ix):

    if string[u_ix] == char:
        if string[l_ix] == char:
            return False
        return True
    
    if string[l_ix] == char:
        return True
    
    return False


with open('pass.txt','r') as f:
    ln = f.readline()
    while(ln):
        
        rg,c,p = ln.split()
        c = c[0]
        l,u = rg.split('-')
        
        if validate(c,p,int(u),int(l)):
            valid += 1

        if validate_v2(c,p,int(u)-1,int(l)-1):
            valid2 += 1

        ln = f.readline()
    
    print(f'Pt.1 {valid}')
    print(f'Pt.2 {valid2}')