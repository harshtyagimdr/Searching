import atexit
import io
import sys
from collections import Counter 
#Contributed by :HARSH TYAGI
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def printRepeating(arr,size) : 
    count = [0] * size 
   
    for i in range(0, size) : 
        if(count[arr[i]] == 1) : 
            print(arr[i], end = " ") 
        else : 
            count[arr[i]] = count[arr[i]] + 1
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        arr = list(map(int,input().strip().split()))
        printRepeating(arr,n+2)
        print()
        
        
                
        