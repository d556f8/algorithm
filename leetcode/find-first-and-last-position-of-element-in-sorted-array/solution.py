from typing import List
import unittest


# FIRST ATTEMPT (FAILED)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        nums_str = "".join(str(num) for num in nums)

        left = self.find_left(nums_str, target)
        right = self.find_right(nums_str, target)

        return [left, right]

    def find_left(self, nums: str, target: int) -> int:
        try:
            return nums.find(str(target))
        except ValueError:
            return -1

    def find_right(self, nums: str, target: int) -> int:
        try:
            return nums.rfind(str(target))
        except ValueError:
            return -1
"""


# SECOND ATTEMPT
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums empty
        if not nums:
            return [-1, -1]

        # nums has only one element
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        left = self.get_left(nums, target)

        if left == -1:
            return [-1, -1]

        right = self.get_right(nums[left:], target) + left

        return [left, right]

    def get_left(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

    def get_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result
"""


# THIRD ATTEMPT
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums empty
        if not nums:
            return [-1, -1]

        # nums has only one element
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        left = self.binary_search(nums, target)
        right = self.binary_search(nums, target, last=True)

        return [left, right]

    def binary_search(self, nums: List[int], target: int, last=False) -> int:
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid

                if last:
                    left = mid + 1
                else:
                    right = mid - 1

            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            {"nums": [5, 7, 7, 8, 8, 10], "target": 8, "expected": [3, 4]},
            {"nums": [5, 7, 7, 8, 8, 10], "target": 6, "expected": [-1, -1]},
            {"nums": [], "target": 0, "expected": [-1, -1]},
        ]

    def test_solution(self):
        solution = Solution()

        for case in self.cases:
            assert (
                solution.searchRange(case["nums"], case["target"]) == case["expected"]
            )


if __name__ == "__main__":
    unittest.main()
