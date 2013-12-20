from MT19937 import Random
from binascii import hexlify, unhexlify
from time import time

PLAIN_TEXT = '123AAAAAAAAAAAAAA'

def xor_encryption():
    keystream = Random (8000)
    ciphertext = ''.join ([chr (ord (pi) ^ (keystream.get() & 0xff)) for pi in PLAIN_TEXT])
    return hexlify (bytes (ciphertext, 'utf-8'))

def keystream (seed, length):
    generator = Random (seed)
    return [generator.get() & 0xff for pi in range (0, length)]

def xor (text, keystream):
    return ''.join ([chr (ord (text[pi]) ^ keystream[pi]) for pi in range (0, len (text))])

def xor_cryptanalysis (ciphertext):
    seed = 0
    ciphers = unhexlify (ciphertext).decode ('utf-8')
    length = len (ciphers)
    while (1):
        print (seed)
        key = keystream (seed, length)
        text = xor (ciphers, key)
        if text[-14:] == 'A' * 14:
            print ('We found you, the seed', seed)
            break
        seed += 1

# gen password reset token: 6 character length in hexa format
def gen_reset_token():
    timestamp = round (time())
    rnd = Random (timestamp)
    token = ''.join ([chr (rnd.get() & 0xff) for pi in range (3)])
    return hexlify (bytes (token, "utf-8")), timestamp

def reverse_reset_token (token):
    current_time = round (time())
    while (1):
        rnd = Random (current_time)
        tmp = ''.join ([chr (rnd.get() & 0xff) for pi in range (3)])
        if str (hexlify (bytes (tmp, "utf-8")), "utf-8") == token:
            print ("The seeder: ", current_time)
            break
        current_time = current_time - 1

if __name__ == "__main__":
   encrypted_msg = xor_encryption()
   print (encrypted_msg)
   xor_cryptanalysis (encrypted_msg)
   print ("password token: ", gen_reset_token())
   reverse_reset_token ("72c2940a")
