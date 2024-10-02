class Solution(object):
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """

        corrected_string = ""

        for i in range(len(s)):
            if ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z') or ('0' <= s[i] <= '9'):
                corrected_string += (s[i])
        corrected_string = corrected_string.lower()
        print(corrected_string)
        for i in range(int((len(corrected_string)) / 2)):
            if corrected_string[i] is not corrected_string[len(corrected_string) - 1 - i]:
                return False


        return True

print(Solution.isPalindrome("A man, a plan, a canal: Panama"))