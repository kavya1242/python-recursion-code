def printnumber(N):
    if N==1:
        return 1
    return printnumber(N-1)+N
N=int(input())
print(printnumber(N))