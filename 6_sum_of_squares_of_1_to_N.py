def sumSquares(N):
    if N==1:
        return 1
    return sumSquares(N-1)+N**2
N=int(input())
print(sumSquares(N))