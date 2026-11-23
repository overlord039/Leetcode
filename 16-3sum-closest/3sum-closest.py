class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target

        return closest