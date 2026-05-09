# Containers with most water
#
# Given an array heights where each element represents the height of a vertical
# line, pick two lines to form a container. Return the maximum area (amount of
# water) the container can hold.
#
# What is area?
# Width × height, where width is the distance between walls, and height is the
# shorter wall (water overflows at the shorter wall).
#
# Example 1:
#
# heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
# solution = 21  # walls at indices 0 and 7 (both height 3): width=7, height=3, area=21
#
# Example 2:
# heights = [1, 2, 1]
# solution = 2  # walls at indices 0 and 2: width=2, height=min(1,1)=1, area=2

from typing import List

EXPONENTIAL = "exponential"
LINEAR = "linear"
CURRENT = LINEAR
VERBOSE = True


class Solution:
    @staticmethod
    def max_area(heights: List[int]) -> int:
        print("")

        if CURRENT == EXPONENTIAL:
            return Solution._exponential(heights)
        if CURRENT == LINEAR:
            return Solution._linear(heights)
        else:
            raise Exception("No solution!")

    @staticmethod
    def _exponential(heights: List[int]) -> int:

        max_area = 0
        count = 0

        for wall_left_index, wall_left_height in enumerate(heights):
            for wall_right_index, wall_right_height in enumerate(heights):
                width = abs(wall_right_index - wall_left_index)
                height = min(wall_right_height, wall_left_height)
                if VERBOSE:
                    print("width", width)
                    print("WIDTH", width)
                area = width * height
                if max_area < area:
                    if VERBOSE:
                        print(
                            f"SUBSTITUTING current area = {max_area} with new value = {area}"
                        )
                    max_area = area
                count += 1

        if VERBOSE:
            print(f"Number of iterations: {count}")

        return max_area

    @staticmethod
    def _linear(heights: List[int]) -> int:
        """Calculates max area with a 2-pointer solution.

        Example:
            Input: heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
            Output: 21
        """

        max_area = 0
        count = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            left_height = heights[left]
            right_height = heights[right]
            height = min(left_height, right_height)
            area = width * height
            if VERBOSE:
                print(
                    f"Width: {width} at left={left} h={left_height}, right={right} h={right_height}"
                )
                print(f"Min height: {height}")

            if left_height <= right_height:
                if VERBOSE:
                    print(f"Moving left pointer {left} +1 to the right")
                left += 1
            else:
                if VERBOSE:
                    print(f"Moving right pointer {right} -1 to the left")
                right -= 1

            if max_area < area:
                if VERBOSE:
                    print(
                        f"SUBSTITUTING current area = {max_area} with new value = {area}"
                    )

                max_area = area
            count += 1
        if VERBOSE:
            print(f"Number of iterations: {count}")

        return max_area
