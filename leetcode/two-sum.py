class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indeks in range(0, len(nums)):
            for indeks2 in range(indeks + 1, len(nums)):
                sum_partial = nums[indeks] + nums[indeks2]
                if sum_partial == target:
                    return [indeks, indeks2]