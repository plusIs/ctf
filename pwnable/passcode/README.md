# passcode
原题说明  
>Mommy told me to make a passcode based login system.  
My initial C code was compiled without any error!  
Well, there was some compiler warning, but who cares about that?  
ssh passcode@pwnable.kr -p2222 (pw:guest)  

# 题解
阅读源代码后发现login函数中使用scanf未使用取地址符，即传递了passcode1，passcode2的数值给scanf，意味着scanf会向passcode1，passcode2的值所指向的地址写入数据。  
在main函数中welcome和login函数是连续调用的，这意味着welcome