#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	int a=0,b=1,c=2;
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	printf("%d\n",key);
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}

