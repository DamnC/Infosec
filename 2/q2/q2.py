import assemble
def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Patch program...
    #0x0633 has 7 nops right before printf
    patch1_offset = int("0633",16)
    #0x05CD has 100 nops! :D
    patch2_offset = int("05CD",16)
    
    #Patch all the things!

    data = list(data)

    patch1 = list(assemble.assemble_file("patch1.asm"))
    data[patch1_offset:patch1_offset+len(patch1)] = patch1

    patch2 = list(assemble.assemble_file("patch2.asm"))
    data[patch2_offset:patch2_offset+len(patch2)] = patch2

    data = ''.join(data)

    #This took way too long...

    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
