# fd
原题说明  
>Daddy told me about cool MD5 hash collision today.  
I wanna do something like that too!  
ssh col@pwnable.kr -p2222 (pw:guest)  

# 题解
阅读源码后发现输入一段字符串后,会执行一个检查函数,之后返回一个数值与`0x21DD09EC`进行比较。逆向算法后可以获得需要输入的字符串  
```C
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}
```
算法见exp.py
计算出应该以`\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\xac\xc9\x9c\xe1`为参数  
于是运行  
```bash
./col $(echo -e '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\xac\xc9\x9c\xe1')
```
