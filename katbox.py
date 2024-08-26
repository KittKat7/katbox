#!python
import sys
import os
import subprocess

APPLETS: list[str] = ["passgen","primefind"]

args: list[str] = sys.argv[1:]
if len(args) < 1:
	args = ["-h"]
#if

path = os.path.dirname(os.path.realpath(__file__)) 

helpString = f"""
KatBox tools

-h, --help      : Show this help text
modify          : Upgrade, or remove KatBox
passgen [LEN]   : Generate a password of LEN characters. Defaults to a length of 10.
primefind [NUM] : Print out NUM of prime numbers. Defaults to 10 primes.
convertbase     : Convert a number from one base to another base. (Useful for Swanson's quizzes)
"""

if args[0] == "-h" or args[0] == "--help":
	print(helpString)
	sys.exit()
elif args[0].lower() == "modify":
	subprocess.run(["bash", "installer.sh"], cwd=path)
	sys.exit()
#if/elif

args = ["python"] + args
args[1] = "" + args[1] + "/" + args[1] + ".py"

subprocess.run(args, cwd=path)
