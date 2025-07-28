#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		# code here
		
		rev= s[::-1]  #end in -1
        if(rev==s):
            return True
        else:
            return False
        
		
