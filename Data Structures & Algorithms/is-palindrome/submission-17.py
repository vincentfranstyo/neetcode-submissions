class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr_s = [alph.lower() for alph in s if alph.isalnum()]
        
        first = 0
        last = len(arr_s) - 1
       
        while first < last:
            if arr_s[first] != arr_s[last]:
                return False
            first += 1
            last -= 1
        
        print(f"{first} {last}")
        
        return True