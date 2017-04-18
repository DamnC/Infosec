def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Fix message...
    curr_xor_res = int("0x9D", 0)
    length = ord(data[0])
    if length > len(data)-2:
       length = len(data)-2
    for c in data[2:2+length]:
            curr_xor_res = curr_xor_res ^ ord(c)
    new_data = chr(length)+chr(curr_xor_res)
    for c in data[2:]:
    	new_data += c
    data = new_data

    with open(path + '.fixed', 'wb') as writer:
        writer.write(data)

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
