from typing import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for c in s:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    

    # Method 2 using sort

    # return sorted(s) == sorted(t)

    # Method 3 using a built in Python function counter

    # return Counter(s) == Counter(t)