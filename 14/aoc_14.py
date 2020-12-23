import sys

def solve_p1(fname):
    mem = {}
    with open(fname,'r') as f:
        ln = f.readline().rstrip()
        mask_bits = {} 
        while(ln):

            # reset the mask
            if ln[:4] == 'mask':
                mask = ln[7:]
                mask_bits = {} 
                for i,v in enumerate(reversed(mask)):
                    if v != 'X':
                        mask_bits[i] = v
            else:
                value = int(ln.split('=')[1][1:])
                for i,v in mask_bits.items():
                    do_mask = (2**i)
                    bit_val = value & do_mask

                    # only flip a bit if it's different than the bit in the mask
                    if do_mask*int(v) != bit_val:
                        value ^= do_mask
                
                # get the address to write value to 
                addr = ln.split('=')[0]
                addr = float(addr[4:len(addr)-2])
                mem[addr] = value
            
            # next line
            ln = f.readline().rstrip()
    
    # sum memory
    acc = float(0)
    for i,v in mem.items():
        acc += v
    return acc 

if __name__ == '__main__':

    print("ans part 1:",solve_p1(sys.argv[1]))