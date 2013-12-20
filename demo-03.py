__author__ = 'tduong'

# try to solve the equation: a = x ^ (x >> b) & c
# b = 2, c = 0xf0 and a = 0x20, space of resolutions = 8bit (255)
def solve8bit():
    x = 0
    while (1):
        # x is right-shifted to 2 bits
        x1 = (x << 2) & 0xff
        x2 = x1 & 0xf0
        x3 = x ^ x2
        if x3 == 0x20:
            break
        x += 1
    print ('x = {0}'.format (x))

# def solve 32 bit
# y = y ^ (y << 15) & 0xefc60000
# a = x ^ (x << b) & c <=> x = [(x << b) & c] ^ a <=> x = (x1 & c) ^ a <=> x = x2 ^ a
# brute the value of last b-bits of x
def solve32bit (a, b, c):
    x = 0
    while (1):
        bin_x = bin(x)[2:]
        x1 = int (bin_x + '0' * b, 2)
        x2 = x1 & c
        tmp_x = (x2 ^ a) & 0xffffffff
        bin_tmp_x = bin(tmp_x)[2:]
        if bin_tmp_x[-len (bin_x):] == bin_x:
            if ((tmp_x << b) & c) ^ tmp_x == a:
                return tmp_x
        x += 1
        if x == 2 ** (32 - b) - 1:
            print ("Arrived in. Break!")
            break

# solve xor function
# a = x ^ (x >> b) <=> a = x ^ x1 <=> x = a ^ x1
# brute the value of x1
def solve_xor(a, b):
    x1 = 1
    while (1):
        tmp_x = a ^ x1
        if (tmp_x >> b) ^ tmp_x == a:
            return tmp_x
        x1 += 1

def reverse_state (rnd):
    y = solve_xor (rnd, 18)
    #print ("y ^= y << 18", y)
    y = solve32bit (y, 15, 0xefc60000)
    #print ("y ^= (y >> 15) & 0xefc60000", y)
    y = solve32bit (y, 7, 0x9d2c5680)
    #print ("y ^= (y >> 7) & 0x9d2c5680", y)
    y = solve_xor (y, 11)
    #print ("y ^= y << 11", y)
    return y

if __name__ == '__main__':
    f = open ('624-values.txt', 'r')
    fout = open ('we-try.txt', 'w')
    values = [int (pi[:-1]) for pi in f.readlines()]
    for pi in range (0, 624):
        tmp = reverse_state (values[pi])
        print ("we know {0}\t{1}\t{2}".format (pi, values[pi], tmp))
        fout.write ("{0}\t{1}\t{2}\n".format (pi, tmp, values[pi]))
    fout.close()
    f.close()
