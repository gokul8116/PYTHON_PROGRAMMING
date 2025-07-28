#User function Template for python3

class Solution:
	def find_fact(self, n):
		# Code here
        if n == 0 or n == 1:
            return 1
        # Recursive case
        return n * self.find_fact(n - 1)
