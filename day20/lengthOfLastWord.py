def lengthOfLastWord(self, s: str) -> int:
    x = s.split() 
    if x:       
        return len(x[-1])  
    return 0 