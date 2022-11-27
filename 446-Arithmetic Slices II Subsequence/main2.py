from collections import defaultdict

# get help from https://www.youtube.com/watch?v=EDHbVuHWljs
class Solution:
  def numberOfArithmeticSlices(self, nums: list[int]) -> int:
    # 2758ms / 68,9MB
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    output = 0
    
    for i in range(n):
      for j in range(i):
        diff = nums[i]-nums[j]
        dp[i][diff] += (1+dp[j][diff])
        output += dp[j][diff]
        
    return output

print( Solution.numberOfArithmeticSlices(Solution, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) ) # 8388331
print( Solution.numberOfArithmeticSlices(Solution, [1,2,1,2,4,1,5,10]) ) # 1
print( Solution.numberOfArithmeticSlices(Solution, [2,4,6,8,10]) ) # 7
print( Solution.numberOfArithmeticSlices(Solution, [7,7,7,7,7]) )  # 16
