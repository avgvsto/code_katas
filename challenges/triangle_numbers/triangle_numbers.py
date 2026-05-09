from pprint import pp
from typing import List

# Triangle numbers
#
# Write a function to count the number of triplets in an integer array nums
# that could form the sides of a triangle.
#
# For three sides to form a valid triangle, all three of these conditions must
# hold:
# (a + b > c),
# (a + c > b),
# and (b + c > a),
# where (a), (b), and (c) are the side lengths.
#
# In other words, the sum of every possible pair must exceed the third side.
#
# The triplets do not need to be unique.
#
# Example:
#
# Input: nums = [11,4,9,6,15,18]
# Output: 10
# Valid combinations
# 4, 15, 18
# 6, 15, 18
# 9, 15, 18
# 11, 15, 18
# 9, 11, 18
# 6, 11, 15
# 9, 11, 15
# 4, 6, 9

EXPONENTIAL = "exponential"
LINEAR = "linear"
CURRENT = LINEAR
VERBOSE = True


class Solution:
    @staticmethod
    def solve(nums: List[int]) -> int:

        result = 10
        if CURRENT == EXPONENTIAL:
            result = Solution._exp(nums)
        elif CURRENT == LINEAR:
            result = Solution._linear(nums)

        return result

    @staticmethod
    def _linear(nums: List[int]) -> int:
        # nums = [4, 10, 21, 14]
        print("")

        ordered = sorted(nums)
        positions_moves = 0
        count = 0
        pp(ordered)

        while len(ordered) > 2:
            max = ordered.pop()
            print(f"Max: {max}, sub-list: {ordered}")
            left = 0
            right = len(ordered) - 1

            positions_moves += 1

            while left < right:
                print(f"    [POINTERS] left={left}, right={right}")
                left_value = ordered[left]
                right_value = ordered[right]
                sides_greater_than_pivot_side = left_value + right_value > max
                positions_moves += 1

                print(f"    [TEST] {left_value}+{right_value}>{max}?")
                if sides_greater_than_pivot_side:
                    valid_combinations_count = right - left

                    print(
                        f"        -> ADDING UP {valid_combinations_count} to the count"
                    )
                    count += valid_combinations_count
                    print(f"        -> Moving right pointer to the left")
                    right -= 1
                else:
                    print(f"        -> Moving left pointer to the right")
                    left += 1

        print(f"\nPositions moves: {positions_moves}")
        return count

    @staticmethod
    def _exp(nums: List[int]) -> int:
        print("")
        solutions = set()
        count = 0

        for side_a in nums:
            for side_b in nums:
                for side_c in nums:
                    a_plus_b = side_a + side_b
                    b_plus_c = side_b + side_c
                    a_plus_c = side_a + side_c

                    count += 1
                    if side_a == side_b or side_b == side_c or side_c == side_a:
                        continue

                    if a_plus_b > side_c and b_plus_c > side_a and a_plus_c > side_b:
                        solutions.add(frozenset([side_a, side_b, side_c]))

        if VERBOSE:
            print(f"Total number of combinations: {count}")
            print("Solutions:")
            pp(solutions)

        return len(solutions)
