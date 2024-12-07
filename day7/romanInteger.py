# def romanToInt(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     romanConversion = {
#         "I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000
#         }
#     sList = s.split()
#     final = 0
#     for i in sList:
#         final += romanConversion[i]
#         return final
#     return final

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    romanConversion = {
        "I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000
        }
    sList = list(s)
    final = 0
    previousValue = 0
    for i in reversed(sList):
        currentValue = romanConversion[i]
        if currentValue < previousValue:
            final -= currentValue
        else:
            final += currentValue
        previousValue = currentValue
    return final
