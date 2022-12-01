class Solution:
    def halvesAreAlike(self, s: str) -> bool:
		# 80ms / 14MB
        s=s.upper()
        l=len(s)
        alike={'A','E','I','O','U'}
        c=0
        for i in range(int(l/2)):
            if(s[i] in alike and not s[l-i-1] in alike):
                c+=1
            if(not s[i] in alike and s[l-i-1] in alike):
                c-=1
            if(c>0):
                if(c > (l/2)+i):
                    return False
            if(c<0):
                if(c*-1 > (l/2)+i):
                    return False
        if c==0:
            return True
        else:
            return False
