class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = "".join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(alpha_str) - 1
        while left<right:
            print(left, right, alpha_str[left], alpha_str[right])
            if alpha_str[left] != alpha_str[right]:
                return False
            left += 1
            right -= 1
        return True

            
        