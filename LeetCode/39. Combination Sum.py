from typing import List
import ast

class Solution:
    def __init__(self):
        self.all_lists = []
        self.all_numbers = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.all_numbers = candidates

        self.find_comb(target, [])

        new_all_list = []

        for l in self.all_lists:
            temp_list = l
            temp_list.sort()
            temp_str = "".join(str(l))
            new_all_list.append(temp_str)

        new_all_list = list(set(new_all_list))



        self.all_lists = []
        self.all_numbers = None

        return [ast.literal_eval(item) for item in new_all_list]

    def find_comb(self, leftover: int, created_list: List[int]):
        for i in self.all_numbers:
            list_copy = created_list.copy()
            list_copy.append(i)
            if leftover - i == 0:
                self.all_lists.append(list_copy)
            elif leftover - i > 0:
                self.find_comb(leftover - i, list_copy)


x = Solution()

print(x.combinationSum([2, 3, 6, 7], 7))
print(x.combinationSum([2,3,5], 8))
print(x.combinationSum([12,3], 15))
