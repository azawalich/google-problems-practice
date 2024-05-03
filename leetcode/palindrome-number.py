class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        y_list = deepcopy(x_list)
        x_list.reverse()
        if x_list == y_list:
            return True
        else:
            return False