# Given a sorted array of integers nums (no duplicates), write a function that
# returns the index of the first element greater or equal to a target.
#
# If there are no results, it returns -1


class BinarySearch:
    @staticmethod
    def find_on(nums, target):

        # O(n)
        count = 0
        for index, num in enumerate(nums):
            count += 1
            if num >= target:
                print(f"\nTotal moves: {count}")
                return index

        print(f"\nTotal moves: {count}")
        return -1

    @staticmethod
    def find(nums, target):
        print("\n")
        print(f"\nNums: {nums}, Target: {target}")

        pointer = 0
        result = -1

        while pointer <= len(nums):
            pointer = int(len(nums) / 2)
            print(f"Pointer={pointer}")

            value_at_pointer = nums[pointer]
            print(f"Value at pointer: {value_at_pointer}")

            if value_at_pointer >= target:
                print(f"    -> Found a result! Move to left")
                result = value_at_pointer
                nums = nums[0:pointer]
            else:
                print(f"    -> Not found a result! Move to right")
                nums = nums[pointer + 1 : len(nums)]
            print(f"New nums: {nums}")

            if len(nums) <= 0:
                break

        return result

    @staticmethod
    def find_index(nums, target):
        print("\n")
        print(f"\nNums: {nums}, Target: {target}")

        left = 0
        right = len(nums) - 1
        pointer = 0
        result = -1
        counter = 0

        move_to = "right"

        while left <= right:
            if move_to == "right":
                pointer = int((right - left) / 2) + left
            else:
                pointer = int((right - left) / 2)

            print(f"  Left={left}, Right={right}, Pointer={pointer}")
            print(f"  Size={right - left + 1}")

            value_at_pointer = nums[pointer]
            print(f"     -> Value at pointer: {value_at_pointer}")

            if value_at_pointer >= target:
                print(f"    -> Found a result! Move to left")
                result = pointer
                right = pointer - 1
                move_to = "left"
            else:
                print(f"    -> Not found a result! Move to right")
                left = pointer + 1
                move_to = "right"
            counter += 1

        print(f"Counter={counter}")
        return result
