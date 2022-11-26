class Solution:
  def twoSum2(self, nums: list[int], target: int) -> list[int]:
    output = list()
    b=0
    for x in range(len(nums)):
      for y in range(len(nums)):
        if(x==y):
          continue
        
        if( (nums[x]+nums[y])==target ):
          output.append(x)
          output.append(y)
          b=1
          break
      if(b==1):
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