import math
from getNumLen import getNumLen
import unittest

def numRev(num: int) -> int:
    negFlag: int = 1
    if num < 0:
        negFlag = -1
        num *= -1
    newNum: int = 0
    while num != 0:
        print(f"newNum : {newNum}")
        print(f"num : {num}")
        newNum = (newNum * 10) + num % 10
        num = math.floor(num / 10)
    print(f"newNum : {newNum}")
    print(f"num : {num}")
    print("-------------------")
    return newNum * negFlag


def isPalindrome(x: int) -> bool:
    return (x == numRev(x))

class getNumLenUT(unittest.TestCase):
    def tests(self):
        self.assertEqual(isPalindrome(9), True)
        self.assertEqual(isPalindrome(923), False)
        self.assertEqual(isPalindrome(99), True)
        self.assertEqual(isPalindrome(919), True)
        self.assertEqual(isPalindrome(123), False)
        self.assertEqual(isPalindrome(1234321), True)
        self.assertEqual(isPalindrome(0), True)

if __name__ == '__main__':
    unittest.main()
