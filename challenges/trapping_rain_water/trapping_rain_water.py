# Write a function to calculate the total amount of water trapped between bars
# on an elevation map, where each bar's width is 1. The input is given as an
# array of n non-negative integers height representing the height of each bar.

# Example:
# - Input: height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
# - Output: 10

#  R
#  L
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#  L  R                       is right >= left? YES! Move left
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#     L  R                    is right >= left? NO!
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#     L     R                 is right >= left? NO!, walls=1
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#     L        R              is right >= left? NO, walls=1,2
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#     L           R           is right >= left? YES!, walls=1,2,2 --> Gotta need to add up water and Move left
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#                 L  R        is right >= left? NO, walls=
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#                 L     R     is right >= left? NO, walls=1
# [3, 4, 1, 2, 2, 5, 1, 0, 2]

#                 L        R  is right >= left? NO, BUT pick the larger, walls=1,0 - IS IT OUT OF RANGE? YES!
# [3, 4, 1, 2, 2, 5, 1, 0, 2]


class Solution:
    def _calculate_dump(self, left, right, in_between):
        return sum([min(left, right) - column for column in in_between])

    def trapped_water(self, walls):

        left, right = 0, 0
        left_wall, right_wall = walls[left], walls[right]
        columns_between_walls = []
        water = 0

        while True:
            if right - 1 > left:
                columns_between_walls.append(walls[right - 1])

            try:
                left_wall, right_wall = walls[left], walls[right]
                print(
                    f"\nLeft={left_wall}[{left}], Right={right_wall}[{right}], Columns={columns_between_walls}\n"
                )
            except IndexError:
                water += self._calculate_dump(
                    left_wall, right_wall, columns_between_walls
                )

                break

            if right_wall >= left_wall:
                left = right
                water += self._calculate_dump(
                    left_wall, right_wall, columns_between_walls
                )
                columns_between_walls = []

            right += 1

        return water

    def brute_force_solution(self, walls):
        print(f"\n\nWalls: {walls}\n")
        total = 0
        number_of_walls = len(walls)

        for index, wall in enumerate(walls):
            max_left = wall
            max_right = wall

            walls_to_the_left = range(index)
            walls_to_the_right = range(index, number_of_walls)
            print(
                f"For wall {index}, to left: {walls_to_the_left}, to right: {walls_to_the_right}"
            )

            for to_left in walls_to_the_left:
                max_left = max(max_left, walls[to_left])

            for to_right in walls_to_the_right:
                max_right = max(max_right, walls[to_right])

            total += min(max_left, max_right) - wall

            print(f"  -> max_to_left={max_left}")
            print(f"  -> max_to_right={max_right}\n")

        return total
