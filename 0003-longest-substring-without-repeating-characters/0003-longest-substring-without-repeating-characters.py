class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        n=len(s)
        s1=""
        count=0
        while i<n:
            if s[i] not in s1:
                s1+=s[i]
                count=max(count,len(s1))
            else:
                s1=s1[s1.index(s[i])+1:]
                continue
            i+=1
        return count