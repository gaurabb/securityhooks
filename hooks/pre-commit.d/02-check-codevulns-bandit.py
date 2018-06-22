#!/usr/bin/env python

'''
This hook will run "bandit" on the python source code to find common security issues in Python code.
Here is what this hook does:
1) Checks an installed version of "sabanditfety"
2) If not found, intalls it
3) Runs bandit on the source code and fails/passes the commit
4) You can bypass this and all other hooks using the "--no-verify" flag with the commit
'''
import os
import re
import shutil
import subprocess
import sys

def install_bandit():
	cmd = 'pip'
	try:
		subprocess.call([cmd, 'install','bandit'])
	except Exception as e:
		print('ERROR: Something went wrong when I tried to install [bandit]\n'\
             'ADVISE: Review the error message below for details:\n{error}'.format(error=str(e)))
		return False
	return True


def run_bandit():
    cmd = "bandit"
    returncode = subprocess.call([cmd, '-r', '.'])
    if returncode == 0:
        return 
    else:
        print(u'ERROR: Code level vulnerabilities detected.\nADVISE: Review the findings and either:\n\t1) fix those or\n\t2) if false positives put a .bandit file in your project’s directory and the exclude: comma separated list of excluded paths. \nCAUTION: you may force the commit with "git commit --no-verify. Not a great idea, is it?".\n')
        sys.exit(1)

def run_bandit_scans():
    print("INFO: Checking for [bandit] installation")
    cmd = "which"
    try:
        returncode=subprocess.call([cmd, 'bandit'])
        if returncode != 0:
            print("INFO: [bandit] is not installed. Trying to install now")
            if install_bandit():
                print("INFO: [bandit] is installed successfully. Running [bandit] now")
                run_bandit()
            else:
                return
        else:
            print("INFO: [bandit] is already installed. Running [bandit] now")
            run_bandit()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print("INFO: [bandit] is not installed. Trying to install now")
            if install_bandit():
                print("INFO: [bandit] is installed successfully. Running [bandit] now")
            else:
                return 
        else:
            print("ERROR: Something went horribly wrong\nADVISE: Review the error message below for details\n{error}".format(error=str(e)))
            return
   
if __name__ == '__main__':
    print("INFO: Running [bandit] open source security scanner")
    run_bandit_scans()