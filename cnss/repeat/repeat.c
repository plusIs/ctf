#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
void getflag()
{
    system("cat flag");
}

int main()
{
    char str[1024];
    memset(str, 0, sizeof(char) * 1024);
    puts("This is a program,which can repeat what you said");
    puts("input something:");
    read(0, str, 1023);
    puts("Haha, your input is:");
    printf(str);
    putchar('\n');
    //printf("%08x\n", *(int*)(0x0804a01c));    
    printf("the length of your input is %d \n", strlen(str));
    return 0;
}