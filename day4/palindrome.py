def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    if x > 0:
        turnToString = str(x)
        return turnToString == turnToString[::-1]