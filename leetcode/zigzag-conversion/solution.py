import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1

        while len(s):
            rows[current_row] += s[0]
            s = s[1:]

            if current_row >= numRows - 1:
                direction = -1
            elif current_row == 0:
                direction = 1

            current_row += direction

        result = "".join(rows)

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            {"s": "PAYPALISHIRING", "numRows": 3, "expected": "PAHNAPLSIIGYIR"},
            {"s": "PAYPALISHIRING", "numRows": 4, "expected": "PINALSIGYAHRPI"},
            {"s": "A", "numRows": 1, "expected": "A"},
        ]

    def test_solution(self):
        solution = Solution()

        for case in self.cases:
            assert solution.convert(case["s"], case["numRows"]) == case["expected"]


if __name__ == "__main__":
    unittest.main()
