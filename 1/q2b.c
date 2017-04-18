#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int input, output;

    if (argc != 2) {
        printf("USAGE: %s <number>\n", argv[0]);
        return -1;
    }

    input = atoi(argv[1]);

    asm ("MOV EBX, %0"
        :
        : "r"(input));

    asm (
        /* Your code starts here. */
	"CMP EBX, 0;"
	"JLE retZero;"
	"CMP EBX, 1;"
	"JE retOne;"
	"MOV ESI, 0;"
	"MOV EDI, 1;"
	"MOV ECX, 2;"
	"_loop:;"
	"MOV EDX, ESI;"
	"ADD EDX, EDI;"
	"MOV ESI, EDI;"
	"MOV EDI, EDX;"
	"ADD ECX, 1;"
	"CMP ECX, EBX;"
	"JLE _loop;"
	"JMP end;"
	"retZero:;"
	"MOV EDX, 0;"
	"JMP end;"
	"retOne:;"
	"MOV EDX, 1;"
	"JMP end;"
	"end:;"
	"MOV EAX, EDX;"
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
