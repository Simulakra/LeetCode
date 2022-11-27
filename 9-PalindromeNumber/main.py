class Solution:
  def isPalindrome(self, x: int) -> bool:
    # 77ms / 13.8MB
    y=str(x)
    for i in range(int(len(y)/2)):
      if(i==0):
        if( y[i] != y[-(i+1):] ):
          return False
      else:
        if( y[i] != y[-(i+1):-i] ):
          return False
    return True

print(Solution.isPalindrome(Solution, 12121))
print(Solution.isPalindrome(Solution, 12345))
print(Solution.isPalindrome(Solution, 1234))
print(Solution.isPalindrome(Solution, -12121))
print(Solution.isPalindrome(Solution, 1111))
print(Solution.isPalindrome(Solution, 11111))