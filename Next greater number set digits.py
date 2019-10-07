import atexit
import io
import sys
from itertools import permutations
#Contributed by :HARSH TYAGI
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def res(x):
    x=list(str(x))
    l=[]
    perm =permutations(x)
    for i in list(perm):
        s=''
        for j in i:
            s+=j
        l.append(int(s))
    l.sort()
    return l
    
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        get=res(n)
        maxi=n
        for i in get:
            if maxi<i:
                maxi=i
                break
        if n<maxi:
            print(maxi)
        else:
            print("not possible")
            
        
            
        