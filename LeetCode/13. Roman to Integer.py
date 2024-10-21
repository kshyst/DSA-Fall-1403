class Solution:
    def romanToInt(self, s: str) -> int:
        final_num = 0

        combinations_tuple = [("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900)]

        for t in combinations_tuple:
            if s.find(t[0]) != -1:
                s = self.removeSubstring(s, t[0])
                final_num += t[1]

        tuples = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]

        index = 0
        while True:
            if s.find(tuples[index][0]) != -1:
                final_num += tuples[index][1]
                s = self.removeSubstring(s, tuples[index][0])
            else:
                index += 1
                if index >= 7:
                    break

        return final_num

    def removeSubstring(self, s: str, substring: str) -> str:
        index = s.find(substring)
        new_string = s[0:index] + s[index + len(substring):len(s)]
        return new_string


x = Solution()
print(x.removeSubstring("kirkhar", "kh"))
