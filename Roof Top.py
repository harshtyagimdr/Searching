import atexit
import io
import sys
#Contributed by :HARSH TYAGI
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        arr = list(input().strip().split())
        for i in range(n):
            arr[i]=int(arr[i])
        c,ans=0,0
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                c+=1
            else:
                c=0
            ans=max(ans,c)
        print(ans)