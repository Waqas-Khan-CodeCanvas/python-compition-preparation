# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# class Solution:
#     def lengthOfLastWord(sefl,s:str)->int:
#         list = s.strip().split(" ")
#         return len(list[-1])
        
        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(" ")[-1])     
        print(len(s.strip().split(" ")[-1]))   
obj = Solution()
obj.lengthOfLastWord("hello world  ")     
obj.lengthOfLastWord("luffy is still joyboy")     
obj.lengthOfLastWord("   fly me   to   the moon  ")     