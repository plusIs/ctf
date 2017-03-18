#!/usr/bin/env python3
import ctypes
import binascii
num = 0x21DD09EC
b = 269488144
a = num - b * 4
b = ctypes.c_uint(b).value
a = ctypes.c_uint(a).value
print(b.to_bytes(4,'little') * 4 + a.to_bytes(4,'little'))
fp = open('exp', 'wb')
fp.write(b.to_bytes(4,'little') * 4)
fp.write(a.to_bytes(4,'little'))
fp.close