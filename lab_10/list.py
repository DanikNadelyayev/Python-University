class Node:

    def __init__(self, item):
        self.next = None
        self.previous = None
        self.item = item


class Stack:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, item):
        self.length += 1
        node = Node(item)
        node.next = self.head
        if self.head is not None:
            self.head.previous = node
        self.head = node

    def size(self):
        print(self.length)

    def print(self):
        node = self.head
        while node is not None:
            print(node.item)
            node = node.next

    def pop(self):
        if self.length == 0:
            return None
        if self.head.next is not None:
            self.head = self.head.next
            self.tail = None

    def sum_of_two_last(self):
        if self.length == 0:
            return None
        item_1 = self.head
        item_2 = item_1.next
        return item_2 + item_1





    def find_node(self, desired) -> bool:
        node = self.head
        self.length = 1
        while node is not None:
            if node.item == desired:
                print(desired, "is found on position:", self.length)
                return True
            node = node.next
            self.length += 1
        print(desired, "is not found")
        return False


s = Stack()

s.push(89)
s.push(10)
s.push(7)
s.push(20)

s.find_node(89)
print()
print()
s.print()
print()
print()
s.size()
