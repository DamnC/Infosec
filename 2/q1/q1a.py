def check_message(path):
    curr_xor_res = int("0x9D", 0)
    with open(path, 'r') as f:
        length = ord(f.read(1))
        wanted_xor = ord(f.read(1))
        msg = f.read()
        if length > len(msg):
            length = len(msg)
	for i in range(length):
            curr_xor_res = curr_xor_res ^ ord(msg[i])
        if (curr_xor_res == wanted_xor):
            return True
    return False


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
