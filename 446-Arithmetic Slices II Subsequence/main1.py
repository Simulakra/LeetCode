class Solution:
  counter = 0
  def numberOfArithmeticSlices(self, nums: list[int]) -> int:
    self.counter = 0

    sscc = 'X'
    for x in nums:
      if(sscc=='X'):
        sscc=str(x)
      elif(sscc!=str(x)):
        sscc='W'
        break

    if(sscc!='W'):
      return self.doMagicMath(self, len(nums)-2)
    else:
      for x in range((len(nums)-1)):
        y = x+1
        while(y<(len(nums)-1)):
          self.checkNextNumber(self,x,y,nums)
          y+=1
      return self.counter

  def doMagicMath(self, count) -> int:
    if(count==1):
      return 1
    temp = count
    allSum = 0
    while(temp>0):
      allSum += temp
      temp -= 1
    return 2*self.doMagicMath(self, count-1) + allSum
  
  def checkNextNumber(self, num1, num2, numz: list[int]):
    diff = numz[num2]-numz[num1]
    srch = numz[num2]+diff
    i=num2+1
    while(True):
      try:
        a = numz.index(srch,i)
        self.counter+=1
        i=a+1
      except:
        break
    if(i>1):
      i=num2+1
      while(True):
        try:
          a = numz.index(srch,i)
          self.checkNextNumber(self,num2,numz.index(srch,i),numz)
          i=a+1
        except:
          break

print( Solution.numberOfArithmeticSlices(Solution, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) ) # 8388331
print( Solution.numberOfArithmeticSlices(Solution, [1,2,1,2,4,1,5,10]) ) # 1
print( Solution.numberOfArithmeticSlices(Solution, [2,4,6,8,10]) ) # 7
print( Solution.numberOfArithmeticSlices(Solution, [7,7,7,7,7]) )  # 16