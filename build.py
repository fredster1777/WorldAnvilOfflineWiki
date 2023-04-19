

import argparse
import subprocess
import sys

try:
    sys.argv[1]
except IndexError:
    print("Missing Commit Message")
    exit(0)


parser = argparse.ArgumentParser(description='My Command')
parser.add_argument('--verbose', action='store_true', help='Display all output')
parser.add_argument('--nobuild', action='store_false', help='Do not build')
parser.add_argument('--nogit', action='store_false', help='No Git Interaction')
parser.add_argument('--clean', action='store_false', help='Delete old builds')
parser.add_argument('-m', help='Git Message')

# Parse the arguments
args = parser.parse_args()



def RunProcess(message):
    print("\nRunning \"" + message + "\"\n")
    proc = subprocess.Popen(message, shell=True)
    proc.wait()

'''
############### Cleanup ###############
if args.clean:
    RunProcess("rm -rf build")

    RunProcess("rm -rf dist")

    RunProcess("rm dist.zip")

    RunProcess("rm *.spec")

    exit(0)
'''
############### Build and ZIP ###############
if args.nobuild:
    RunProcess("pyinstaller --onefile Source/WorldAnvilOfflineWiki.py")

    RunProcess("zip dist.zip dist//WorldAnvilOfflineWiki")



############### GIT ###############
if args.nogit:
    RunProcess("git add *")

    RunProcess("git commit -m " + sys.argv[2])

    RunProcess("git push")





