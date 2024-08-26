class Solution:
    def longestPalindrome(self, s: str) -> str:
        toCheck = ""
        result = ""
        resultSize = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                toCheck+=s[j]
                if toCheck==toCheck[::-1] and len(toCheck)>resultSize:
                    result=toCheck
                    resultSize=len(toCheck)
            toCheck=""
        return result