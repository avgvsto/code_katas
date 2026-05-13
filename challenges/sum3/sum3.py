# Given an input integer array nums, write a function to find all unique
# triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct
# indices, and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure
# that the resulting list does not contain any duplicate triplets.
#
# The order of the triplets and the order of the elements within the triplets
# do not matter.

# Example:
# Input --> nums = [-1,0,1,2,-1,-1]
# Output --> [[-1,-1,2],[-1,0,1]]


# Solution design
#
#
# nums   = [-1,0,1,2,-1,-1]
# sorted = [-1,-1,-1,0,1,2]
#
#       L        R
# -1, [-1,-1,0,1,2]    find_for=1  --> -1+2 is it 1? YES! add a solution
#                                      move left (skip it while equals to previous left)
#                                      move right (skip it while equals to previous left)
#
#            L R
# -1, [-1,-1,0,1,2]    find_for=1  --> 0+1 is it 1? YES! add a solution
#                                      move left (skip it while equals to previous left)
#                                      move right (skip it while equals to previous left)
#
#      L R
#  0, [1,2]          find_for=0  --> 1+2 is it 1? it's too big
#                                      move right
#


class Solution:
    OPTIMAL = True

    def find_sum3_triplets(self, nums):
        if self.OPTIMAL is False:
            return self._all_combinations(nums)
        else:
            return self._optimal_combinations(nums)

    def _optimal_combinations(self, nums):
        """Attempt to improve O(n^3)

        Usually O(n log n)
        """

        numbers = sorted(nums)
        solutions = []
        print(f"\n\nNUMBERS: {numbers}\n")

        previous = None
        for index, target in enumerate(numbers):
            if target == previous:
                continue

            sub_numbers = numbers[index + 1 : len(numbers)]
            if len(sub_numbers) < 2:
                continue

            print(f"TARGET={target}, SUB_NUMBERS={sub_numbers}")
            left, right = 0, len(sub_numbers) - 1
            neg_target = target * -1
            while left < right:
                print(
                    f"    left={sub_numbers[left]}[{left}], right={sub_numbers[right]}[{right}]"
                )

                left_item, right_item = sub_numbers[left], sub_numbers[right]

                left_right_sum = sum((left_item, right_item))
                if left_right_sum == neg_target:
                    solution = [target, left_item, right_item]
                    solutions.append(solution)
                    print(f"    [SOLUTION FOUND] {solution}")

                if left_right_sum > neg_target:
                    print("    [MOVE] right-1")
                    future_right = right_item
                    while right_item == future_right:
                        right -= 1
                        future_right = sub_numbers[right]
                else:
                    print("    [MOVE] left+1")
                    future_left = left_item
                    while left_item == future_left:
                        left += 1
                        future_left = sub_numbers[left]

            previous = target

        return solutions

    def _all_combinations(self, nums):
        """This solution is the brute-force approach

        Time complexity: O(n^3)
        """

        triplets = set()
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                for k, num_k in enumerate(nums):
                    if any((i == j, i == k, j == k, k == i)):
                        continue

                    if sum((num_i, num_j, num_k)) == 0:
                        i, j, k = sorted([num_i, num_j, num_k])
                        triplets.add(f"{i},{j},{k}")

        final_format = []
        for triplet in triplets:
            items = triplet.split(",")
            final_format.append([int(item) for item in items])

        return final_format
