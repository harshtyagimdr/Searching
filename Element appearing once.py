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
        l=[]
        for i in arr:
            if len(l)==0:
                l.append(i)
            else:
                if i==l[-1]:
                    l.pop()
                else:
                    l.append(i)
        print(*l)