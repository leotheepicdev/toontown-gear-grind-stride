#!C:\Panda3D-1.11.0-x64-astron\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cxfreeze==0.1.1','console_scripts','cxfreeze'
__requires__ = 'cxfreeze==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cxfreeze==0.1.1', 'console_scripts', 'cxfreeze')()
    )
