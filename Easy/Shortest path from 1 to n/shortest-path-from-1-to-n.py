#User function Template for python3

class Solution:
    def minimumStep (self,n):

        #completing the function here

        if n<3:

            return n-1

        return 2+self.minimumStep(n//3)+self.minimumStep(n%3)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends