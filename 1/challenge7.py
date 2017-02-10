# https://cryptopals.com/sets/1/challenges/7

from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES

def main():
    key = b"YELLOW SUBMARINE"
    plain = b64decode(open('7.txt').read())

    cipher = AES.new(key, AES.MODE_ECB)
    print(cipher.decrypt(plain).decode('utf-8'))

if __name__ == '__main__':
    main()
