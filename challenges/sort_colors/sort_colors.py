# Write a function to sort a given integer array nums in-place (and without
# the built-in sort function), where the array contains n integers that are
# either 0, 1, and 2 and represent the colors red, white, and blue. Arrange
# the objects so that same-colored ones are adjacent, in the order of red,
# white, and blue (0, 1, 2).
#
# Input:
#     nums = [2,1,2,0,1,0,1,0,1]
#
# Output:
#     [0,0,0,1,1,1,1,2,2]
#
#
# Solution design
#
# The first idea is to do a basic-sorting algorithm, like bubble-sort.
# - it definitely works
# - performance is O(n^2), can we do better? better is O(n)
#
# Second approach could be 2-pointer walk through
#
#  L               R     is it item[L] 2? YES --> move item[L] to the last! R--
# [2,1,2,0,1,0,1,0,1]
#
#  L             R       is it item[L] 2/0? NO --> L++
# [1,2,0,1,0,1,0,1,2]
#
#    L           R       is it item[L] 2/0? YES --> move item[L] to the last! R--
# [1,2,0,1,0,1,0,1,2]
#
#    L         R         is it item[L] 2/0? YES --> move item[L] to the first! L++
# [1,0,1,0,1,0,1,2,2]
#
#      L       R         is it item[L] 2/0? NO --> L++
# [0,1,1,0,1,0,1,2,2]
#
#        L     R         is it item[L] 2/0? YES --> move item[L] to the first! L++
# [0,1,1,0,1,0,1,2,2]
#
#          L   R         is it item[L] 2/0? YES --> move item[L] to the first! L++
# [0,0,1,1,1,0,1,2,2]
#
#            L R         is it item[L] 2/0? YES --> move item[L] to the first! L++
# [0,0,1,1,1,0,1,2,2]
#
#              L
#              R         BREAK
# [0,0,0,1,1,1,1,2,2]


VALID_COLORS = frozenset((0, 1, 2))


def sort_numbers_as_colors(nums):

    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left]
        if current not in VALID_COLORS:
            raise TypeError("Only integers 0, 1, 2 allowed")

        print(f"left={current}[{left}], right={nums[right]}[{right}]")
        if current == 2:
            new_last = nums.pop(left)  # O(n)
            nums.append(new_last)  # O(n)
            right -= 1
            print("  RIGHT -- (2 found!)")
        elif current == 0:
            new_first = nums.pop(left)  # O(n)
            nums.insert(0, new_first)  # O(n)
            left += 1
            print("   LEFT ++ (0 found)")
        else:
            print("   LEFT ++ (1 found)")
            left += 1
        print("")
