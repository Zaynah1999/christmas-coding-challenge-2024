def longestCommonPrefix(self, strs: List[str]) -> str:
        stringer = ""
        shortest = len(min(strs, key=len))
        for j in range(shortest):
            for i in range(1, len(strs)):
                values_hold = (strs[i-1][j] == strs[i][j])                    
                if not values_hold:
                    return stringer
            stringer += strs[0][j]
        else:
            return stringer