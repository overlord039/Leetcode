class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def dfs(start,com,total):
            if total==target:
                result.append(com[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                com.append(candidates[i])
                dfs(i,com,total+candidates[i])
                com.pop()
        dfs(0,[],0)
        return result

        