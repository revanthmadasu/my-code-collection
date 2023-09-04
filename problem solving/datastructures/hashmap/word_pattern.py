class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_chars = list(pattern)
        words = s.split(' ')
        if len(words) != len(pattern_chars):
            return False
        n = len(words)
        converter = {}
        result = True
        for i in range(n):
            pattern_char = pattern_chars[i]
            word = words[i]
            if not converter.has_key(pattern_char):
                converter[pattern_char] = word
            else:
                if not converter[pattern_char] == word:
                    result = False
                    break
        reverse_converter = {}
        for key in converter.keys():
            word = converter[key]
            if reverse_converter.has_key(word):
                result = False
                break
            reverse_converter[word] = key
        return result
