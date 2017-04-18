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
	"MOV EDI, ESP;"
	"CMP EBX, 1;"
	"JLE retZero;"
	"MOV EAX, EBX;"
	"MOV ESI, EBX;"
	"MOV ECX, 2;"
	"_loop:;"
	"XOR EDX, EDX;"
	"PUSH EAX;"
	"DIV ECX;"
	"CMP EDX, 0;"
	"JE Divides;"
	"POP EAX;"
	"JMP notDivides;"
	"Divides:;"
	"JMP _loop;"
	"notDivides:;"
	"CMP EAX, 1;"
	"JE end;"
	"ADD ECX, 1;"
	"CMP ECX, ESI;"
	"JL _loop;"
	"JMP end;"
	"retZero:;"
	"MOV ECX, 0;"
	"end:;"
	"MOV EAX, ECX;"
	"MOV ESP, EDI;"
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
