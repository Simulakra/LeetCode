class Solution:
  def twoSum2(self, nums: list[int], target: int) -> list[int]:
    # 574ms / 14.8MB
    output = list()
    for x in range(len(nums)):
      c=target-nums[x]
      try:
        d=nums.index(c, x+1)
        output = [x,d]
      except:
        continue
      break
    return output

aaaa = Solution.twoSum(Solution , [2,7,11,15], 9)
print(aaaa) # [0,1]
aaaa = Solution.twoSum(Solution , [3,2,4], 6)
print(aaaa) # [1,2]
aaaa = Solution.twoSum(Solution , [3,3], 6)
print(aaaa) # [0,1]
aaaa = Solution.twoSum(Solution , [-3,4,3,90], 0)
print(aaaa) # [0,2]