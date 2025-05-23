'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
import re

#O(n)
# def isPalindrome(self, s: str) -> bool:
#         s = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower()
#         s = s.replace(" ", "")
#         if(len(s) < 1):
#             return True
#         else:
#             for i in range(len(s)):
#                 l = s[i]
#                 r = s[len(s)-1-i]
#                 if(l!=r):
#                     return False
#             return True


#O(n)
def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower()
        s = s.replace(" ", "")
        r = s[::-1]
        if(r == s):
            return True
        else:
    
            return False

print(isPalindrome(None, "A man, a plan, a canal: Panama"))
