#!D:\Panda3Ds\Panda3D-1.11.0-x64-astron\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'xdis==6.1.0','console_scripts','pydisasm'
__requires__ = 'xdis==6.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('xdis==6.1.0', 'console_scripts', 'pydisasm')()
    )
