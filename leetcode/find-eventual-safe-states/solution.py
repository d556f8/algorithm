import unittest
from typing import List


class Solution:
    def __init__(self):
        self.neg = []
        self.pos = []
        self.graph = []

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      self.graph = graph
      for node in graph:
        # [1, 2]


    def search(self, node: List[int], history: List[int]):
      for item in node:
        if item in self.neg:
          continue
        if item in history:
          self.neg.append(item);
          continue
        
        self.search()

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            {
                "graph": [[1, 2], [2, 3], [5], [0], [5], [], []],
                "expected": [2, 4, 5, 6],
            },
            {"graph": [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], "expected": [4]},
        ]

    def test_solution(self):
        solution = Solution()

        for case in self.cases:
            assert solution.eventualSafeNodes(case["s"]) == case["expected"]


if __name__ == "__main__":
    unittest.main()
