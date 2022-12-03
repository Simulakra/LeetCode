import operator

class Solution:
  def frequencySort(self, s: str) -> str:
    # 203ms / 15.4MB
    tmp = {}
    for x in range(len(s)):
      if(s[x] in tmp):
        tmp[s[x]] +=1
      else:
        tmp[s[x]]=1
    
    tmp = dict( sorted(tmp.items(), key=operator.itemgetter(1),reverse=True))
    s_tmp=""
    for x in tmp.keys():
      s_tmp+=str(x)*tmp[x]
    return s_tmp
