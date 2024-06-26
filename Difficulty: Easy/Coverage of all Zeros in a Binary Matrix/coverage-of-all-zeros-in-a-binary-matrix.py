#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
		ans = 0
		n = len(matrix)
		m = len(matrix[0])
		
		for i in range(n):
		    for j in range(m):
		        if matrix[i][j]==0:
		            if j>0 and matrix[i][j-1]==1:
		                ans+=1
		            if j<m-1 and matrix[i][j+1]==1:
		                ans+=1
		            if i>0 and matrix[i-1][j]==1:
		                ans+=1
		            if i<n-1 and matrix[i+1][j]==1:
		                ans+=1
		                
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends