Roman_arabic = {
'I': 1,
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = list(s)
        S_list_arabic = [''] * len(s_list)
        for single_number in range(0, len(s_list)):
            Temp_arabic = Roman_arabic[s_list[single_number]]
            if single_number > 0:
                if s_list[single_number] in ['V', 'X'] and s_list[single_number-1] == 'I':
                    Temp_arabic = Roman_arabic[s_list[single_number]] - 1
                    S_list_arabic[single_number-1] = 0
                elif s_list[single_number] in ['L', 'C'] and s_list[single_number-1] == 'X':
                    Temp_arabic = Roman_arabic[s_list[single_number]] - 10
                    S_list_arabic[single_number-1] = 0
                elif s_list[single_number] in ['D', 'M'] and s_list[single_number-1] == 'C':
                    Temp_arabic = Roman_arabic[s_list[single_number]] - 100
                    S_list_arabic[single_number-1] = 0
            S_list_arabic[single_number] = Temp_arabic
        return sum(S_list_arabic)
