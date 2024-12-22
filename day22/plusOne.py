def plusOne(self, digits: List[int]) -> List[int]:
    convertToInt = int(''.join(map(str, digits))) + 1
    convertToList = list(map(int, str(convertToInt)))
    return convertToList



    