#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		
		
# 		rev=int(str(n)[::-1])
# 		return rev
        
        if(n<=1):
            return n
            
        rev=0;
        
        while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n=n//10
            
        return rev   
