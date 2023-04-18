

import argparse
import subprocess
import sys

if not sys.argv[0]:
    exit("Enter Commit Message")



parser = argparse.ArgumentParser(description='My Command')
parser.add_argument('--verbose', action='store_true', help='Display all output')
parser.add_argument('--nobuild', action='store_false', help='Do not build')
parser.add_argument('--nogit', action='store_false', help='No Git Interaction')
parser.add_argument('--clean', action='store_false', help='Delete old builds')
# Parse the arguments
args = parser.parse_args()


'''
############### Cleanup ###############
if args.clean:
    output = subprocess.run("rm -rf build", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())

    output = subprocess.run("rm -rf dist", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())

    output = subprocess.run("rm dist.zip", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())

    output = subprocess.run("rm WorldAnvilOfflineWiki.spec", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())

    exit(0)
'''
############### Build and ZIP ###############
if args.nobuild:
    output = subprocess.run("pyinstaller --onefile Source/WorldAnvilOfflineWiki.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())

    output = subprocess.run("zip dist.zip dist//WorldAnvilOfflineWiki", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())



############### GIT ###############
if args.nogit:
    output = subprocess.run("git add *", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())


    output = subprocess.run("git commit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())
    none = input("in4")

    output = subprocess.run("git push", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if args.verbose: print(output.stdout.decode())
    none = input("in5")






