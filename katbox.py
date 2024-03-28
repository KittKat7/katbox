#!python
import sys
import os
import subprocess


args: list[str] = sys.argv[1:]

helpString = """
passgen [length (defaults to 10)]
primefind [numberOfPrimes (defaults to 10)]
"""

if "-h" in args or "--help" in args:
    print(helpString)
    sys.exit()

args = ["python"] + args
args[1] = "" + args[1] + "/" + args[1] + ".py"

path = os.path.dirname(os.path.realpath(__file__)) 

subprocess.run(args, cwd=path)
