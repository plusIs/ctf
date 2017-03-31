# fd
原题说明  
>Mommy! what is a file descriptor in Linux?  
try to play the wargame your self but if you are ABSOLUTE beginner, follow this tutorial link:  https://www.youtube.com/watch?v=blAxTfcW9VU  
ssh fd@pwnable.kr -p2222 (pw:guest)

# 题解
看代码后发现了read函数
```C
int fd = atoi( argv[1] ) - 0x1234;
int len = 0;
len = read(fd, buf, 32);
if(!strcmp("LETMEWIN\n", buf)){
	printf("good job :)\n");
	system("/bin/cat flag");
	exit(0);
}
```
查百科知read的函数原型为  
```C
ssize_t read(int fd,void * buf ,size_t count);
```
fd为文件描述符  
value   name  
0       STDIN_FILENO  
1       STDOUT_FILENO  
2       STDERR_FILENO  
使fd为0后便可以控制标准输入拿到flag  
于是运行  
```bash
./fd 4660
```
之后输入`LETMEWIN`拿到flag