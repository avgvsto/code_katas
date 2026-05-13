from challenges.sum3.sum3 import Solution


def test_it_finds_triplets_that_add_up_zero():

    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -1]

    triplets = solution.find_sum3_triplets(nums)

    assert [-1, -1, 2] in triplets
    assert [-1, 0, 1] in triplets
    assert len(triplets) == 2


def test_it_finds_triplets_crazy():

    solution = Solution()
    nums = [-1, -2, 0, 1, 2, -1, -1, -3, 3, 4, -2]

    triplets = solution.find_sum3_triplets(nums)

    test_triplets = [set(triplet) for triplet in triplets]
    assert set([-1, -1, 2]) in test_triplets
    assert set([-1, 0, 1]) in test_triplets
    assert set([-2, 0, 2]) in test_triplets
    assert set([-3, 0, 3]) in test_triplets
    assert set([-2, -1, 3]) in test_triplets
    assert set([-2, -2, 4]) in test_triplets
    assert set([-1, -3, 4]) in test_triplets
    assert set([-3, 2, 1]) in test_triplets
    assert len(triplets) == 8
