__author__ = 'tduong'

from Crypto.Cipher import AES
from Crypto import Random
from binascii import hexlify, unhexlify
from struct import pack

KEY = Random.new().read (16)

class CTREncryption:
    def __init__ (self, nonce=''):
        if type (nonce) is not int:
            self.nonce = Random.new().read (8)   # 8-byte random Nonce
        else:
            self.nonce = pack ("<Q", nonce)

    def _keystream (self, counter):
        # 8-byte counter in little-endian format || 8 byte-nonce in little-endian format
        enc = AES.new (KEY, AES.MODE_ECB)
        keystream = enc.encrypt (self.nonce + pack ("<Q", counter % 256))
        return keystream

    def xor (self, msg, key):
        return ''.join ([chr (msg[pi] ^ key[pi]) for pi in range (0, len (msg))])\
            .encode ('latin-1')

    def keystream (self, length):
        key = b''
        for pi in range (length // 16 + 1):
            key += self._keystream (pi)
        return key

    def encrypt (self, plaintext):
        key = self.keystream (len (plaintext))
        return self.xor (plaintext, key)

    def decrypt (self, ciphertext):
        key = self.keystream (len (ciphertext))
        return self.xor (ciphertext, key)

if __name__ == "__main__":
    aes_ctr = CTREncryption()
    encrypted = hexlify (aes_ctr.encrypt (b'hello world'))
    print ("Encrypted: ", encrypted)
    print ("Decrypted: ", aes_ctr.decrypt (unhexlify (encrypted)))

