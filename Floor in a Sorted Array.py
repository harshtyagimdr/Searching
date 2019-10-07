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
        n,k=(int(i) for i in input().split())
        arr = list(map(int,input().strip().split()))
        if k<arr[0]:
            print(-1)
        else:
            c=0
            for i in arr:
                if i>k:
                    break
                c+=1
            print(c-1)
        