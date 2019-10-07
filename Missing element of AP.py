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
        arr = list(map(int,input().strip().split()))
        if len(arr)==2:
            print((arr[0]+arr[1])//2)
        else:
            res = [arr[i + 1] - arr[i] for i in range(len(arr)-1)]
            ind=res.index(max(res))
            no=arr[ind+1]-min(res)
            print(no)