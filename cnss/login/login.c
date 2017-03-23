#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int get_name_data(int num)
{
    char str[100];
    int user_code;
    user_code = num;
    memset(str, 0, sizeof(char) * 100);
    puts("We will use your name to check whether you are an admin");
    puts("Please input your name:");
    scanf("%100s", str);
    for (int i = 0; i < strlen(str); ++i)
    {
        user_code += str[i];
    }
    printf("Hello %s\n", str);
    sleep(2);
    printf("Your user_code is %d\n", user_code);
    sleep(2);
    return user_code;
}
void get_flag(int name_data)
{
    int tmp1, tmp2, result;
    tmp1 = name_data;
    srand(tmp1);
    tmp2 =  rand();
    tmp2 = tmp2 % 1325;
    printf("The key of your user_code is %d\n", tmp2);
    sleep(1);
    puts("Checking......");
    sleep(3);
    result += tmp1 + tmp2;
    if (result == 1792)
    {
        puts("Checking sucess!Welcome back!");
        system("/bin/sh");
    }
    else
    {
        puts("Checking failed");
        puts("try again!");
    }
}

int main()
{
    puts("I know you have already learned how to build a payload to overflow the stack");
    puts("In this program, I'll tell you how to build a payload to exploit uninitialized variables");
    sleep(2);
    puts("-------------------------------------------------");
    sleep(1);
    puts("when you notice a program use an uninitialized variables,");
    puts("you can use the stack data of previous function to achieve your goal");
    puts("Please press Enter to continue");
    while(getchar() != '\n');
    int name_data = get_name_data(0);
    get_flag(name_data);
    return 0 ;
}