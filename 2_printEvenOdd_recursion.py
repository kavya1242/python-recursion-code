#Write a recursive function (or a standalone script with a function) that takes an integer n and returns the sum of all numbers from 1 to n
p = []
h = []
def printEvenOdd(n, i):
    
    if i == n + 1:
        result = p + h[::-1]
        print(*(result))
        return
    if i % 2 == 0:
        p.append(i)
    else:
        h.append(i)
    printEvenOdd(n, i + 1)
n=int(input())
printEvenOdd(n,1)
