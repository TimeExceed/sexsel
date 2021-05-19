#!/usr/bin/python3
from pathlib import Path
import subprocess as sp

if __name__ == '__main__':
    cwd = Path.cwd()
    cmd = [
        'docker', 'run', '--rm',
        '-v', '%s:/opt/code' % cwd,
        'taoda-base',
        'scons',
    ]
    print(cmd)
    sp.run(cmd).check_returncode()
    
