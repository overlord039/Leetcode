class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        def dfs(start,com,total):
            if total==target:
                result.append(com[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                com.append(candidates[i])
                dfs(i+1,com,total+candidates[i])
                com.pop()
        dfs(0,[],0)
        return [list(x) for x in result]

        