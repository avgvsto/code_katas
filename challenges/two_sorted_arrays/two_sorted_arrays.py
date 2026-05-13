# Given a sorted array of integers nums, determine if there exists a pair of
# numbers that sum to a given target.

# Example
#
# Input:
#     nums = [1,3,4,6,8,10,13]
#     target = 13
#
# Output:
#     True # (3 + 10 = 13)
#
# Example 2
#
# Input:
#     nums = [1,3,4,6,8,10,13]
#     target = 6
#
# Output:
#     False


# Solution design:
#
#  L             R
# [1,3,4,6,8,10,13]    target=13, R+L > target? yes
#
#  L          R
# [1,3,4,6,8,10,13]    target=13, R+L > target? no
#
#    L        R
# [1,3,4,6,8,10,13]    target=13, R+L > target? no, FOUND!


class Solution:
    def cuadratic(self, nums, target):

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if i == j:
                    continue
                if num_i + num_j == target:
                    return True

        return False

    def find_2_sum(self, nums, target):

        print(f"\nNUMS: {nums}\n")
        left, right = 0, len(nums) - 1

        while left < right:
            print(f"left={nums[left]}[{left}], right={nums[right]}[{right}]")
            result = sum((nums[left], nums[right]))
            if result == target:
                return True

            if result >= target:
                print("    Moving RIGHT -1\n")
                right -= 1
            else:
                print("    Moving LEFT +1\n")
                left += 1
        return False
