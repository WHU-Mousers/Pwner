import re
import pwnlib
from pwn import *

'''
This module aims add more feature to tube class.
Based on Autopwn : less_tube.py
'''

def add_features(src):
    features = [l64, l32, verify_valid, extnum]
    for feature in features:
        setattr(pwnlib.tubes.tube.tube, feature.__name__, feature)
    assert type(src) != int
    return src

def verify_valid(self, func, **kwargs):
    return func(self, kwargs)


def l64(self):
    return self.verify_valid(lambda ex, args: u64(ex.recvuntil("\x7f")[-6:].ljust(8,"\x00")))

def l32(self):
    return self.verify_valid(lambda ex, args: u32(ex.recvuntil("\xf7")[-4:].ljust(4,"\x00")))

def extnum(self, base = 10):  
    res = []
    if base == 10:
        pattern = re.compile(r'\d+')
    elif base == 16:
        pattern = re.compile(r"[0-9a-fA-F]{4,}")
    else:
        return None

    src = self.recvline()
    res = re.findall(pattern, src)
    for i in range(0, len(res)):
        res[i] = int(res[i], base=base)
    return res