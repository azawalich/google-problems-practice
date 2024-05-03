class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_positive = [i for i in nums if i > 0]
        nums_positive.sort(reverse=True)
        nums_negative = [i for i in nums if i < 0]
        if len(nums_positive) > 0 and len(nums_negative) > 0:
            min_number = min(nums_negative)
            absolute_nums_negative = [abs(l) for l in nums_negative]
            absolute_nums_negative.sort(reverse=True)
            max_number = max(nums_positive)
            if max_number == abs(min_number):
                return max_number
            else:
                counter = -1
                for single_number in nums_positive:
                    if single_number in absolute_nums_negative:
                        counter = single_number
                        break
                return counter
        else:
            return -1