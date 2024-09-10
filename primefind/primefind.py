
def main(args: list[str]):
    numOfPrimes: int = 10

    try:
        numOfPrimes = int(args[0])
    except:
        numOfPrimes = 10

    listOfPrimes: list[int] = []

    def isPrime(num: int) -> bool:
        for i in range(1, num):
            if num % i == 0 and i != 1 and i != num:
                return False
            #if
        #for
        return True
    #isPrime

    num: int = 1
    while len(listOfPrimes) < numOfPrimes:
        if isPrime(num):
            listOfPrimes.append(num)
        #if
        num+=1
    #while

    print(listOfPrimes)

