#User function Template for python3
from functools import cmp_to_key
class Solution:

	def printLargest(self, n, arr):
	    # code here
	    a = "".join(sorted(arr, key= cmp_to_key(lambda a,b : -1 if (a+b) > (b+a) else 1 )))
	    return str(int(a))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends