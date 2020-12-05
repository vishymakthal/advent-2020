
res = 1
def check_slope(x_inc,y_inc):

    trees = 0
    with open('slope.txt','r') as f:
        ln = f.readline().rstrip()
        x = 0
        while(ln):

            if ln[x] == '#':
                trees += 1
        
            x += x_inc
            x = x % len(ln)
            
            for n in range(y_inc):
                ln = f.readline().rstrip()

        print(trees)
        return trees

res *= check_slope(1,1)
res *= check_slope(3,1)
res *= check_slope(5,1)
res *= check_slope(7,1)
res *= check_slope(1,2)

print(res)