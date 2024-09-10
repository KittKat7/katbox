#!python
import sys
import os
import subprocess

import passgen.passgen as passgen
import primefind.primefind as primefind
import convertbase.convertbase as convertbase

class KatBox:
    targets: dict[str, list[object]] = {
        "--help,-h": [None, "\n\t Display help message"],
        "--modify,-m": [None, "\n\t Shows install dialogue, allows installing, upgrading, or removing. (Install and upgrade are from github)"],
        "passgen": [passgen, "[LEN] \n\t Generates a password of length LEN, or defaults to 10"],
        "primefind": [primefind, "[LEN] \n\t Prints out LEN prime numbers, defaults to 10"],
        "convertbase": [convertbase, "{NUM}[_BASE] {NEWBASE} \n\t Converts NUM of base BASE or 10 to the same number in base NEWBASE"],
        "dice": [None, "[NUM1, NUM2, ..., NUMn] \n\t For every NUM, generates a random number between (including) 1 and NUM"],
    }

    @staticmethod
    def helpStr() -> str:
        string: str = ""
        for key in list(KatBox.targets.keys()):
            string += f"{key} {KatBox.targets[key][1]}\n"
        return string
    #helpStr

    @staticmethod
    def main(args: list[str]):

        args: list[str] = args[1:]
        if len(args) < 1:
            args = ["-h"]
        #if

        path = os.path.dirname(os.path.realpath(__file__)) 

        if args[0] == "-h" or args[0] == "--help":
            print(KatBox.helpStr())
            sys.exit()
        elif args[0].lower() == "--modify":
            subprocess.run(["bash", "installer.sh"], cwd=path)
            sys.exit()
        elif args[0][0] == "-":
            sys.exit()
        #if/elif

        if args[0] in list(KatBox.targets.keys()):
            KatBox.targets[args[0]][0].main(args[1:])
        #if
    #main
#KatBox

KatBox.main(sys.argv)
