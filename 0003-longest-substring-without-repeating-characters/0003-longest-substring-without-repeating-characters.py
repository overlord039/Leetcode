class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)):
            a=set()
            for j in range(i,len(s)):
                if s[j] in a:
                    break
                a.add(s[j])
                count=max(count,j-i+1)
        return count
                

        