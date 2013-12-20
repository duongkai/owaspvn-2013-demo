class Random:
    length = 624
    mersenne = [0] * length
    bit_mask_32 = 2 ** 32 - 1
    
    def __init__ (self, seed):
        self.set (seed)

    def set (self, seed):
        self.index = 0
        self.mersenne[0] = seed
        for pi in range (1, self.length):
            self.mersenne[pi] = (1812433253 * (self.mersenne[pi - 1] ^ \
                (self.mersenne[pi - 1] >> 30)) + pi) & self.bit_mask_32

    def get (self):
        if self.index == 0:
            self.seeding()
        y = self.mersenne[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18
        self.index = (self.index + 1) % self.length
        #return y, self.mersenne[self.index - 1], self.index - 1
        return y

    def seeding (self):
        for pi in range (0, self.length):
            y = (self.mersenne[pi] & 0x80000000) + \
                (self.mersenne[(pi + 1) % self.length] & 0x7fffffff)
            self.mersenne[pi] = self.mersenne[(pi + 397) % self.length] ^ (y >> 1)
            if y % 2 != 0:
                self.mersenne[pi] = self.mersenne[pi] ^ 2567483615