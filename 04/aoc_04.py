import re

def check_pass(p):

    if not p.get('byr', False) or not re.match(r'^((19[2-9][0-9])|(200[0-2]))$', p['byr']):
        return False

    if not p.get('iyr', False) or not re.match(r'^((201[0-9])|(2020))$', p['iyr']):
        return False
    
    if not p.get('eyr', False) or not re.match(r'^((202[0-9])|(2030))$', p['eyr']):
        return False
    
    if not p.get('hgt', False) or not re.match(r'^((((1[5-8][0-9])|(19[0-3]))cm)|(((59)|(6[0-9])|(7[0-6]))in))$', p['hgt']):
        return False

    if not p.get('hcl', False) or not re.match(r'^(#[a-f0-9]{6})$', p['hcl']):
        return False

    if not p.get('ecl', False) or not re.match(r'^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$', p['ecl']):
        return False

    if not p.get('pid', False) or not re.match(r'^([0-9]{9})$', p['pid']):
        return False

    return True

def validate(f_name):
    cnt = 0
    ln_cnt = 0 
    cmp_pass = {}

    with open(f_name,'r') as f:
        cur = f.readline()
        while(cur):

            if cur != '\n':
                for s in cur.rstrip().split(' '):
                    if s[:3] != 'cid':
                        cmp_pass[s[:3]] = s[4:] 
            else:
                
                if check_pass(cmp_pass):
                    cnt += 1
                cmp_pass = {}            

            cur = f.readline()
            ln_cnt += 1
    return cnt

# print(validate('test.txt'))
print(validate('p1.txt'))