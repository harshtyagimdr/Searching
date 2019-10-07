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
        n,m=(int(i) for i in input().split())
        l=[]
        r=[]
        arr = [[int(j) for j in input().split()] for i in range(n)]
        m=max(arr[n-1])
        r.append(m)
        for i in range(n-2,-1,-1):
            
            for j in arr[i]:
                if len(l)==0:
                    if j<m:
                        l.append(j)
                else:
                    if j<m and j>l[-1]:
                        l.pop()
                        l.append(j)
            if len(l)!=0:
                m=l[-1]
                l=[]
                r.append(m)
            
        if len(r)==n:    
            print(sum(r))
        else:
            print(0)
                
        
        