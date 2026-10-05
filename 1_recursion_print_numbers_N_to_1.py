N=4
def printNumber(N,i):
    if N==i-1:
        return
    print(N)
    printNumber(N-1,i)
printNumber(N,1)