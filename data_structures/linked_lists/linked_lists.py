class Pointer:
    def __init__(self):
        self.points_to = None

    def point(self, node):
        self.points_to = node

    def next(self):
        return self.points_to


class Node:
    def __init__(self, value):
        self.item_value = value
        self.next_item = None

    def next(self):
        return self.next_item

    def value(self):
        return self.item_value

    def point(self, node):
        self.next_item = node

    def __repr__(self):
        return f"[NODE|value: {self.value()}]"


class LinkedList:
    def __init__(self):
        self.head = Pointer()
        self.tail = Pointer()

    def append(self, value):

        new_node = Node(value)

        head_node = self.head.next()
        if not head_node:
            self.head.point(new_node)
        tail_node = self.tail.next()
        if not tail_node:
            self.tail.point(new_node)
        else:
            tail_node.point(new_node)
            self.tail.point(new_node)

    def pop(self):

        current = self.head.next()
        previous = None

        if not current:
            return

        while current.next():
            previous = current
            current = current.next()

        self.tail.point(previous)

        if previous:
            previous.point(None)
        else:
            self.head.point(None)

        return current.value()

    def pop_first(self):

        first = self.head.next()

        if not first:
            return

        value = first.value()
        next = first.next()
        self.head.point(next)
        if not next:
            self.tail.point(None)

        return value

    def prepend(self, value):

        new_node = Node(value)

        current_head = self.head.next()
        new_node.point(current_head)

        self.head.point(new_node)

        tail_node = self.tail.next()
        if not tail_node:
            self.tail.point(new_node)

    def insert(self, value, index):
        print("")
        new_node = Node(value)
        current = self.head.next()
        position = 0

        if not current:
            if index == 0:
                self.append(value)
            return

        while True:
            if position == index - 1:
                current_next = current.next()
                new_node.point(current_next)
                current.point(new_node)
                if not current_next:
                    self.tail.point(new_node)
                break
            position += 1

            current = current.next()

    def search(self, value):

        current = self.head.next()
        position = 0

        if not current:
            return

        while current.next():
            position += 1
            if current.value() == value:
                return {
                    "position": position,
                    "value": current.value(),
                    "node_id": f"[NODE|value:{current.value()}]",
                }
            current = current.next()

    def search_by_index(self, index):

        current = self.head.next()
        position = 0

        if not current:
            return

        while True:
            if position == index:
                return {
                    "position": position,
                    "value": current.value(),
                    "node_id": f"[NODE|value:{current.value()}]",
                }
            position += 1
            current = current.next()
            if not current:
                break
