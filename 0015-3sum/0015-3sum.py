class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        l = set()

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s > 0:
                    right -= 1

                elif s < 0:
                    left += 1

                else:
                    l.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return [list(x) for x in l]