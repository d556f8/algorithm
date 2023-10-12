import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
      before = None
      result = 0
      
      for c in s:
        if (c == 'I'):
          before = 1
          result += 1
        elif (c == 'V'):
          if (before == 1):
            result += 3
            before = None
            continue
          before = 5
          result += 5
        elif (c == 'X'):
          if (before == 1):
            result += 8
            before = None
            continue
          before = 10
          result += 10
        elif (c == 'L'):
          if (before == 10):
            result += 30
            before = None
            continue
          before = 50
          result += 50
        elif (c == 'C'):
          if (before == 10):
            result += 80
            before = None
            continue
          before = 100
          result += 100
        elif (c == 'D'):
          if (before == 100):
            result += 300
            before = None
            continue
          before = 500
          result += 500
        elif (c == 'M'):
          if (before == 100):
            result += 800
            before = None
            continue
          before = 1000
          result += 1000
        else:
          result += 0

      return result
        

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            {"s": "III", "expected": 3},
            {"s": "LVIII", "expected": 58},
            {"s": "MCMXCIV", "expected": 1994},
        ]

    def test_solution(self):
        solution = Solution()

        for case in self.cases:
            assert solution.romanToInt(case["s"]) == case["expected"]


if __name__ == "__main__":
    unittest.main()
