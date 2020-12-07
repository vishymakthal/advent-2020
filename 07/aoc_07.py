import re


'''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

held_by = {
    'bw' : ['lr','do'],
    'my' : ['lr','do'],
    'sg' : ['bw','my'],
    'do' : ['sg'],
    'vp' : ['sg'],
    'fb' : ['do','vp'],
    'db' : ['do','vp']
}

hold = {
}

def how_many_bags(bag_color):

    cnt = 0
    can_hold = set()
    st = [bag_color]
    initial = bag_color
    while st:
        cur = st.pop(0)
        for b in held_by.get(cur, []):
            if b != initial:
                st.append(b)
            can_hold.add(b)
    
    return len(can_hold)      

tot = 0
def how_many_bags_in(bag_color):

    if not hold.get(bag_color, None):
        return 0

    tot = 0
    for b in hold.get(bag_color,[]):
        tot += b[1] + b[1]*how_many_bags_in(b[0])
    
    return tot 
            

with open('rules.txt') as f:

    ln = f.readline().rstrip()

    while(ln):

        r = re.findall(r'[a-z]+ [a-z]+(?= bag)', ln)
        r_p2 = re.findall(r'[0-9] [a-z]+ [a-z]+', ln)
        if r and r[1] != 'no other':
            
            hold[r[0]] = [(r_p2[i][2:],int(r_p2[i][0])) for i in range(len(r_p2))]
            for i in range(1,len(r)):
                
                
                if held_by.get(r[i], None):
                    held_by[r[i]].append(r[0])
                else:
                    held_by[r[i]] = [r[0]]
        
        ln = f.readline().rstrip()

    print(how_many_bags('shiny gold'))
    print(how_many_bags_in('shiny gold'))

