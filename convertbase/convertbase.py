"""
--- Base Convert ---
Convert any number to a given base, (up to base 16/hexadecimal).

How To Use:
If no oldbase is provided, the default will be 10.
number[_oldbase]-newbase
TODO
"""
import sys
args = sys.argv[1:]

if "-h" in args or "--help" in args:
    print(__doc__)
    sys.exit()

ack = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
kca = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

def div(num, base):
    rem = num % base
    n = str(rem)
    print(str(num) + "/" + str(base) + "=" + str(int(num/base)) + "r" + str(rem))
    if num < base:
        n = str(num)
        if n in kca.keys():
            n = kca[n]
        return n
    
    if n in kca.keys():
        n = kca[n]
    return div(int(num / base), base) + n

def mult(num, base):
    ars = []
    res = 0
    for i in range(len(num)):
        n = 0
        p = len(num) - 1 - i
        if num[i].upper() in ack.keys():
            n = ack[num[i].upper()]
        else:
            n = num[i]
        re = int(n) * pow(base, p)
        res += re
        ars.append(str(re))
        print(n + "*" + str(pow(base, p)) + "=" + str(re))
    out = ""
    for i in range(len(ars)):
        out += ars[i]
        if i != len(ars) - 1:
            out += "+"
    out += "=" + str(res)
    
    return out

def main():
    swanson: bool = False
    if "--swanson" in args:
        swanson = True
        args.remove("--swanson")

    inp: str = args[0]

    num: int
    obase: int
    nbase: int

    try:
        if "_" in inp:
            num = int(inp.split("_")[0])
            obase = int(inp.split("_")[1].split("-")[0])
            nbase = int(inp.split("_")[1].split("-")[1])
        else:
            num = int(inp.split("-")[0])
            nbase = int(inp.split("-")[1])
            obase = 10
    except:
        print("Invalid input")
        sys.exit()
    
    
    if obase == 10:
        print(str(num) + "_" + str(obase) + " >> _" + str(nbase) + " = " + str(div(num, nbase)))
    elif nbase == 10:
        print(str(num) + "_" + str(obase) + " >> _" + str(nbase) + " = " + str(mult(str(num), obase)))
    else:
        print(str(num) + "_" + str(obase) + " >> _" + str(nbase) + " = " + str(div(int(mult(str(num), obase).split("=")[1]), nbase)))

if __name__ == "__main__":
    main()


# while True:
#     toten = False
#     ogbase = 10
#     ognum = input("Enter number.base: ")
#     if ognum.upper() == "EXIT" or ognum.upper() == "Q":
#         sys.exit()
    
#     try:
#         if "." in ognum:
#             ogbase = int(ognum.split(".")[1])
#             ognum = ognum.split(".")[0]
#             nbase = 10
#             toten = True
#         else:
#             ognum = int(ognum)
#             nbase = int(input("Enter new base: "))
#     except:
#         print("ERR: NaN")
#         continue

#     if toten:
#         print(str(ognum) + "_" + str(ogbase) + " >> _" + str(nbase) + " = " + str(mult(str(ognum), ogbase)))
#     else:
#         print(str(ognum) + "_" + str(ogbase) + " >> _" + str(nbase) + " = " + str(div(ognum, nbase)))

