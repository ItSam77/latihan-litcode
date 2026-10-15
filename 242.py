class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [ord(char) for char in s]
        t = [ord(char) for char in t]
        s.sort()
        t.sort()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return (sum(s) == sum(t))
        