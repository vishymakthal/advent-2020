


def check_group(responses):

    s = {}
    cnt = 0
    for r in responses:
        for c in r:
            s[c] = s.get(c,0) + 1

    for q in s:
        if s[q] == len(responses):
            cnt += 1
    return cnt


with open('in.txt') as f:

    ln = f.readline()
    resps = []
    tot = 0

    while(ln):

        if ln == '\n':
            tot += check_group(resps)
            resps = []
        else:
            resps.append(ln.rstrip())

        ln = f.readline() 

    print(tot)