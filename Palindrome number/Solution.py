class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        if a==a[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """