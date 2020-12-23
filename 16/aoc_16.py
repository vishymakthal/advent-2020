import sys
from rich import print


def read_input(fname):
    with open(fname,'r') as f:
        ln = f.readline().rstrip()
        nln_cnt = 0
        rules = []
        nearby_tickets = []
        
        while(nln_cnt < 3):
            if nln_cnt == 0:
                rules.append(ln.split(':')[1].split('or'))
            if nln_cnt == 1:
                # skip the "your ticket" line
                f.readline().rstrip()
                my_ticket = f.readline().rstrip()
                
                # skip the "nearby ticket" line
                f.readline().rstrip()
                f.readline().rstrip()
                nln_cnt += 1 
                ln = f.readline().rstrip()
            if nln_cnt == 2:
                if ln[0] != 'n':
                    nearby_tickets.append(ln)
            
            ln = f.readline().rstrip()
            if not ln:
                nln_cnt += 1
        return rules,my_ticket,nearby_tickets

def solve_p1(rules,tickets):

    valid_range = set()
    acc = 0
    for rule in rules:
        for _range in rule:
            lower,upper = _range.split('-')
            for n in range(int(lower),int(upper)+1):
                valid_range.add(n)

    for t in tickets:
        for n in map(lambda x: int(x), t.split(',')):
            if n not in valid_range:
                acc += n
    return acc 

if __name__ == '__main__':

    rules,my_ticket,nearby_tickets = read_input(sys.argv[1])
    print("Answer part 1:",solve_p1(rules,nearby_tickets))