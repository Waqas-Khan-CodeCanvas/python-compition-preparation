# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:

# Input: s = "110"
# Output: true
 
 
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segments = s.split('0')
        count = 0
        
        for seg in segments:
            if seg:
                count += 1
        
        return count <= 1

obj = Solution()
result = obj.checkOnesSegment("1001")
result1 = obj.checkOnesSegment("1001")

print(result)
print(result1)