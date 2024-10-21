class Solution:
    def intToRoman(self, num: int) -> str:

        final_str = ""

        while True:
            if num >= 1000:
                final_str += "M"
                num -= 1000
                continue
            elif num >= 500:
                if num >= 900:
                    final_str += "CM"
                    num -= 900
                else:
                    final_str += "D"
                    num -= 500
                continue
            elif num >= 100:
                if num >= 400:
                    final_str += "CD"
                    num -= 400
                else:
                    final_str += "C"
                    num -= 100
                continue
            elif num >= 50:
                if num >= 90:
                    final_str += "XC"
                    num -= 90
                else:
                    final_str += "L"
                    num -= 50
                continue
            elif num >= 10:
                if num >= 40:
                    final_str += "XL"
                    num -= 40
                else:
                    final_str += "X"
                    num -= 10
                continue
            elif num >= 5:
                if num >= 9:
                    final_str += "IX"
                    num -= 9
                else:
                    final_str += "V"
                    num -= 5
                continue
            elif num >= 1:
                if num >= 4:
                    final_str += "IV"
                    num -= 4
                else:
                    final_str += "I"
                    num -= 1
            else:
                break

        return final_str

x = Solution()
print(x.intToRoman(58))