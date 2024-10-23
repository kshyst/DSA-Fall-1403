from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        all_permutations = []

        if len(digits) == 0:
            return []

        if digits[0] != 1:
            for i in num_to_letter[digits[0]]:
                all_permutations.append(i)

        index = 1

        while index < len(digits):
            if digits[index] == '1' or digits[index] == '0':
                continue

            new_temp_all_permutations = []

            for i in all_permutations:
                for j in num_to_letter[digits[index]]:
                    new_temp_all_permutations.append(i + j)

            all_permutations = new_temp_all_permutations
            index +=1

        return all_permutations



x = Solution()
print(x.letterCombinations("23"))


