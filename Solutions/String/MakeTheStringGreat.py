class Solution:
    def makeGood(self, s: str) -> str:
        count =0 
        ss = ''
        l=0
        while (len(s) != l):
            l=len(s)
            for i in range(len(s)-1):
                if s[i].lower() == s[i+1].lower() and ((s[i].isupper() and s[i+1].islower()) or (s[i].islower() and s[i+1].isupper())):
                    count+=1
                    s = s[:i]+s[i+2:]
                    break
            print(count)
        return s

        # return s
