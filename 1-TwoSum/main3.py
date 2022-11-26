class Solution:
  def twoSum2(self, nums: list[int], target: int) -> list[int]:
    # 78ms / 15.2MB
    h = {}
    for i, num in enumerate(nums):
      n = target - num
      if n not in h:
          h[num] = i
      else:
          return [h[n], i]

aaaa = Solution.twoSum(Solution , [2,7,11,15], 9)
print(aaaa) # [0,1]
aaaa = Solution.twoSum(Solution , [3,2,4], 6)
print(aaaa) # [1,2]
aaaa = Solution.twoSum(Solution , [3,3], 6)
print(aaaa) # [0,1]
aaaa = Solution.twoSum(Solution , [-3,4,3,90], 0)
print(aaaa) # [0,2]