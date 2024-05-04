class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n_grams_words = []
        shortest_word = 200
        for single_word in strs:
            if len(single_word) < shortest_word:
                shortest_word = len(single_word)
            temp_list = []
            for n_gram in range(1,len(single_word)+1):
                for single_index in range(0,len(single_word)):
                    if single_index < len(single_word):
                        temp_list.append(single_word[single_index:single_index+n_gram])
            n_grams_words.append(temp_list)
        common = set(n_grams_words[0])
        for single_set in range(1, len(n_grams_words)):
            common = common.intersection(set(n_grams_words[single_set]))
        final_list = []
        for single_common in common:
            final_list.append(single_common)
        
        final_list = sorted(final_list, key=len)
        if len(final_list) > 0:
            return final_list[-1]
        else:
            return ""
