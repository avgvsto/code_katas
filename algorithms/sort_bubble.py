# Design solution

# [1, 4, 5, 2, 6]

#  c=current, n=next
#
#
#  c  n             is c>n? NO
# [1, 4, 5, 2, 6]
#
#     c  n          is c>n? NO
# [1, 4, 5, 2, 6]
#
#        c  n       is c>n? YES --> SWAP
# [1, 4, 5, 2, 6]
#
#           c  n    is c>n? NO      larger was bubbled-up
# [1, 4, 2, 5, 6]
#
#  c  n             is c>n? NO
# [1, 4, 2, 5]
#
#     c  n          is c>n? YES --> SWAP
# [1, 4, 2, 5]
#
#        c  n       is c>n? NO      larger was bubbled-up
# [1, 2, 4, 5]
#
#  c  n             KEEP GOING
# [1, 2, 4]


def sort_bubble(iterable):

    to_sort = [item for item in iterable]
    for i in reversed(range(len(iterable))):
        sublist = range(i)

        print(f"\nSORTING {to_sort}")
        print("========================")
        print(f"    \nSUBLIST: {sublist}")
        print("========================")
        for index in sublist:
            current = to_sort[index]
            print(f"    current={current}[{index}]")
            next_index = index + 1
            if next_index > len(sublist):
                print("    SKIPPING")
                continue
            next_item = to_sort[next_index]
            print(f"Current={current}[{index}], Next={next_item}[{next_index}]")

            if current > next_item:
                print(
                    f"    SWAPPING indexes {index}<>{next_index}, because {current}>{next_item}"
                )
                to_sort[index] = next_item
                to_sort[next_index] = current

    return to_sort
