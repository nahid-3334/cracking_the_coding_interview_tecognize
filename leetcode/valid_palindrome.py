class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())  #remove non alphanumeric 
        s = s.lower() #lower case
        #sorted array 2 pointer approach
        start=0
        end=len(s)-1 #o(n)
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True  