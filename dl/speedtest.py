
import warnings

DEPRECATED_MSG = ('The file speedtest.py has been deprecated in favor of '
                  'speedtest.py\nand is available for download at:\n\n'
                  'https://raw.githubusercontent.com/SSHAnakSolo/autoscript/'
                  'master/dl/speedtest.py')


if __name__ == '__main__':
    raise SystemExit(DEPRECATED_MSG)
else:
    try:
        from speedtest import *
    except ImportError:
        raise SystemExit(DEPRECATED_MSG)
    else:
        warnings.warn(DEPRECATED_MSG, UserWarning)
