class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        bigger_num, smaller_num = None, None

        if len(num1) >= len(num2):
            bigger_num = num1
            smaller_num = num2
        else:
            bigger_num = num2
            smaller_num = num1

        numbers_array = [0] * 1000
        outer_index = 0

        for i in range(len(smaller_num)):
            i_number = ord(smaller_num[len(smaller_num) - i - 1]) - 48
            inner_index = outer_index
            for j in range(len(bigger_num)):
                j_number = ord(bigger_num[len(bigger_num) - j - 1]) - 48
                numbers_array[inner_index] += i_number * j_number
                inner_index += 1

            outer_index += 1


        index = 0
        final_string = ""
        while numbers_array[index] != 0 or numbers_array[index + 1] != 0 or numbers_array[index + 2] != 0:
            final_string = chr(numbers_array[index] % 10 + 48) + final_string
            numbers_array[index + 1] += int(numbers_array[index] / 10)
            index += 1

        print(numbers_array)
        # print(final_string)

        if final_string == "":
            return "0"
        return final_string

x = Solution()

print(x.multiply("6", "501"))
