import pytest

from data_structures.linked_lists.linked_lists import LinkedList, SimpleLinkedList


class TestSimple:
    def test_it_is_constructed(self):

        ll = SimpleLinkedList()

        assert ll.head.next() is None
        assert ll.tail.next() is None

    class TestAppend:
        def test_it_appends_first_element(self):

            ll = SimpleLinkedList()

            ll.append(10)

            head = ll.head.next()
            tail = ll.tail.next()
            assert tail is not None
            assert head is not None
            assert head.value() == tail.value() == 10
            assert head.next() == tail.next() is None

        def test_it_appends_second_element(self):

            ll = SimpleLinkedList()
            ll.append(10)
            ll.append(20)

            first = ll.head.next()

            assert first is not None
            second = first.next()
            assert second is not None
            assert second.value() == 20
            assert second.next() is None
            assert ll.head.next() == first
            assert ll.tail.next() == second

        def test_it_appends_third_element(self):

            ll = SimpleLinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)

            first = ll.head.next()

            assert first is not None
            second = first.next()
            assert second is not None
            assert second.value() == 20
            assert second.next() is not None
            third = second.next()
            assert third.value() == 30
            assert third.next() is None

            assert ll.head.next() == first
            assert ll.tail.next() == third

    class TestPop:
        def test_it_pops_the_last_element(self):

            ll = SimpleLinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)

            item = ll.pop()

            assert item == 30
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 20
            assert tail_item.next() is None
            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 10
            assert head_item.next().value() == 20

        def test_it_returns_none_if_empty(self):

            ll = SimpleLinkedList()

            item = ll.pop()

            assert item is None

        def test_it_pops_single_item(self):

            ll = SimpleLinkedList()
            ll.append(10)

            item = ll.pop()

            assert item == 10
            head_item = ll.head.next()
            assert head_item is None
            tail_item = ll.tail.next()
            assert tail_item is None

    class TestPopFirst:
        def test_it_removes_the_first_item(self):

            ll = SimpleLinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)

            result = ll.pop_first()

            assert result == 10
            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 20
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 30

        def test_it_removes_the_only_item(self):

            ll = SimpleLinkedList()
            ll.append(10)

            result = ll.pop_first()

            assert result == 10
            first_item = ll.head.next()
            assert first_item is None
            tail_item = ll.tail.next()
            assert tail_item is None

    class TestPrepend:
        def test_it_adds_to_an_empty_list(self):

            ll = SimpleLinkedList()

            ll.prepend(99)

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 99
            assert head_item.next() is None
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 99
            assert tail_item.next() is None

        def test_it_adds_to_the_beggining_of_all_items(self):

            ll = SimpleLinkedList()

            ll.prepend(99)
            ll.prepend(33)
            ll.prepend(11)

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 11
            assert head_item.next().value() == 33

            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 99
            assert tail_item.next() is None

    class TestInsert:
        def test_it_inserts_an_item_into_a_specific_index(self):
            ll = SimpleLinkedList()
            ll.append(123)
            ll.append(456)
            ll.append(789)

            ll.insert(000, 1)

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 123
            assert head_item.next().value() == 000
            assert head_item.next().next().value() == 456
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 789
            assert tail_item.next() is None

        def test_it_inserts_an_item_into_an_empty_list(self):
            ll = SimpleLinkedList()

            ll.insert(123, 0)

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 123
            assert head_item.next() is None
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 123
            assert tail_item.next() is None

        def test_it_inserts_at_the_end(self):
            ll = SimpleLinkedList()
            ll.append(123)
            ll.append(456)
            ll.append(789)

            ll.insert(000, 3)

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 123
            assert head_item.next().value() == 456
            assert head_item.next().next().value() == 789
            assert head_item.next().next().next().value() == 000
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 000
            assert tail_item.next() is None

    class TestSearchByValue:
        def test_it_returns_item_and_position(self):

            ll = SimpleLinkedList()
            ll.append(123)
            ll.append(456)
            ll.append(789)

            result = ll.search(456)

            assert result == {
                "value": 456,
                "position": 2,
                "node_id": "[NODE|value:456]",
            }

        def test_it_returns_nothing_when_item_does_not_exist(self):

            ll = SimpleLinkedList()
            ll.append(11)
            ll.append(33)

            result = ll.search(123)

            assert result is None

        def test_it_returns_nothing_when_empty(self):

            ll = SimpleLinkedList()

            result = ll.search(123)

            assert result is None

    class TestSearchByIndex:
        def test_it_returns_item_and_position(self):

            ll = SimpleLinkedList()
            ll.append(123)
            ll.append(456)
            ll.append(789)

            result = ll.search_by_index(1)

            assert result == {
                "value": 456,
                "position": 1,
                "node_id": "[NODE|value:456]",
            }

        def test_it_returns_nothing_when_item_does_not_exist(self):

            ll = SimpleLinkedList()
            ll.append(123)
            ll.append(456)
            ll.append(789)

            result = ll.search_by_index(34)

            assert result is None

        def test_it_returns_nothing_when_empty(self):

            ll = SimpleLinkedList()

            result = ll.search_by_index(0)

            assert result is None

    class TestReverse:
        def test_it_reverses_the_list(self):

            ll = SimpleLinkedList()
            ll.append(1)
            ll.append(2)
            ll.append(3)
            ll.append(4)
            ll.append(5)
            ll.append(6)
            ll.append(7)

            ll.reverse()

            head_item = ll.head.next()
            assert head_item is not None
            assert head_item.value() == 7
            assert head_item.next().value() == 6
            assert head_item.next().next().value() == 5
            assert head_item.next().next().next().value() == 4
            assert head_item.next().next().next().next().value() == 3
            assert head_item.next().next().next().next().next().value() == 2
            assert head_item.next().next().next().next().next().next().value() == 1
            tail_item = ll.tail.next()
            assert tail_item is not None
            assert tail_item.value() == 1
            assert tail_item.next() is None


class TestLinkedList:
    class TestAppend:
        def test_it_appends_first_element(self):

            ll = LinkedList()

            ll.append(10)

            head = ll.head.next()
            tail = ll.tail.next()
            assert tail is not None
            assert head is not None
            assert head.value() == tail.value() == 10
            assert head.next() == tail.next() is None

    class TestSequence:
        def test_it_is_iterable(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)

            result = [item for item in ll]

            assert result == [10, 20, 30]

        def test_it_is_subscriptable_by_index(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            result = ll[1]

            assert result == 20

        def test_it_raises_with_negative_index(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            with pytest.raises(NotImplementedError):
                ll[-1]

        def test_it_is_subscriptable_by_slices(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            result = ll[1:3]

            assert result == [20, 30]

        def test_it_is_subscriptable_by_positive_slices(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            result = ll[1:3]

            assert result == [20, 30]

        def test_it_is_subscriptable_by_slice_start_out_of_range(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            result = ll[10:30]

            assert result == []

        def test_it_is_subscriptable_by_slice_end_out_of_range(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            result = ll[1:300]

            assert result == [20, 30, 40]

        def test_it_is_subscriptable_with_step(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)
            ll.append(50)
            ll.append(60)
            ll.append(70)

            result = ll[1:6:3]

            assert result == [20, 50]

        def test_it_raises_on_start_negative(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            with pytest.raises(NotImplementedError):
                ll[-1:300]

        def test_it_raises_on_end_negative(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            with pytest.raises(NotImplementedError):
                ll[1:-300]

        def test_it_raises_on_step_negative(self):

            ll = LinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.append(40)

            with pytest.raises(NotImplementedError):
                ll[1:300:-2]
