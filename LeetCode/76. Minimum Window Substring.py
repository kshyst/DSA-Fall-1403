import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0

        if s == t:
            return s

        if len(t) > len(s):
            return ""

        if len(t) == len(s):
            found = True

            temp_substring = s
            for char in range(len(t)):
                if t[char] not in temp_substring:
                    found = False
                    break
                else:
                    temp_substring_list = list(temp_substring)
                    temp_substring_list.pop(temp_substring.find(t[char]))
                    temp_substring = ''.join(temp_substring_list)
            if not found:
                return ""
            else:
                return s

        substrings = []

        while right < len(s):
            while left <= right:
                found = True
                temp_substring = s[left:right + 1]
                for char in range(len(t)):
                    if t[char] not in temp_substring:
                        found = False
                        break
                    else:
                        temp_substring_list = list(temp_substring)
                        temp_substring_list.pop(temp_substring.find(t[char]))
                        temp_substring = ''.join(temp_substring_list)
                if found:
                    substrings.append(s[left:right + 1])
                    left += 1
                else:
                    break

            right += 1

        #return substrings

        min_len = math.inf
        selected_substring = ""
        for i in substrings:
            if min_len > len(i):
                min_len = len(i)
                selected_substring = i

        return selected_substring


x = Solution()
print(x.minWindow("ADOBECODEBANC", "ABC"))
print(x.minWindow("bdab", "ab"))
