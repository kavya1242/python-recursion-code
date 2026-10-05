arr=list(map(int, input().split()))
def rev(i,arr,N):
    if i>=N//2:
        print(arr)
        return  
    arr[i],arr[N-i-1]=arr[N-i-1],arr[i]
    return rev(i+1,arr,N)
N=len(arr)
rev(0,arr,N)