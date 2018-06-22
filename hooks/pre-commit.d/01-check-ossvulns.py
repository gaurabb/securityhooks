#!/usr/bin/env python

'''
This hook will run "safety" on the dependencies of this project as listed in the requirements.txt file
Here is what this hook does:
1) Checks an installed version of "safety"
2) If not found, intalls it
3) Runs the script and fails/passes the commit
4) You can bypass this and all other hooks using the "--no-verify" flag with the commit
'''
import os
import re
import shutil
import subprocess
import sys
import tempfile
import platform


def install_safety():
    cmd = 'pip'
    try:
        subprocess.call(cmd, 'install safety')
    except OSError as e:
        print('ERROR: Something went wrong when I tried to install [safety]\nADVISE: Review the error message below for details:\n{error}'.format(error=str(e)))
        return False
    return True


def check_safety_oss():
    print("INFO: Checking for [safety] installation")
    cmd = "where" if platform.system() == "Windows" else "which"
    try:
        subprocess.call([cmd, 'safety'])
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print("INFO:[safety] is not installed. Trying to install now")
            if install_safety():
                print("INFO: [safety] is installed successfully. Running [safety] now")
            else:
                return 
		else:
            print("ERROR: Something went horribly wrong\nADVISE: Review the error message below for details\n{error}".format(error=str(e)))
            return
    except:
        print('ERROR: [safety] cannot be installed')
        return

    cmd = "safety"
    returncode = subprocess.call([cmd, 'check', '--full-report'])
    if returncode == 0:
		return 
	else:
		print(u'ERROR: Insecure dependencies have been detected.\nADVISE: Please fix them\nCAUTION: you may force the commit with "git commit --no-verify".\n')
		sys.exit(1)


if __name__ == '__main__':
    print("INFO: running [safety] open source security scanner")
    check_safety_oss()
	