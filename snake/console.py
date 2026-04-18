
import os
import sys


def getTerminalSize():
    env = os.environ
    
    if sys.platform == 'win32':
        try:
            columns, lines = os.get_terminal_size()
            return int(columns), int(lines)
        except (OSError, AttributeError):
            pass
    else:
        import fcntl
        import termios
        import struct

        def ioctl_GWINSZ(fd):
            try:
                cr = struct.unpack(
                    'hh',
                    fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234')
                    )
            except:
                return
            return cr

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        return int(cr[1]), int(cr[0])
    
    cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])
