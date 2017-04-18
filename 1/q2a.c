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
	"CALL fib;"
	"JMP realEnd;"
	"fib:;"
	"CMP EBX, 0;"
	"JLE retZero;"
	"CMP EBX, 1;"
	"JE retOne;"
	"PUSH EBX;"
	"SUB EBX, 1;"
	"CALL fib;"
	"XOR EDX, EDX;"
	"ADD EDX, EAX;"
	"POP EBX;"
	"PUSH EBX;"
	"PUSH EDX;"
	"SUB EBX, 2;"
	"CALL fib;"
	"POP EDX;"
	"POP EBX;"
	"ADD EDX, EAX;"
	"JMP end;"
	"retZero:;"
	"MOV EAX, 0;"
	"RET;"
	"retOne:;"
	"MOV EAX, 1;"
	"RET;"
	"end:;"
	"MOV EAX, EDX;"
	"RET;"
	"realEnd:;"
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
