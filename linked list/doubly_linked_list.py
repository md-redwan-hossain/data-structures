class Node:
    def __init__(self, data=None, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after


class LinkedList:
    def __init__(self):
        self.reverse = False
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            temp = self.head
            self.head = new_node
            new_node.after = temp
            temp.before = new_node

        self.size += 1

    def append(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.prepend(data)
        else:
            self.size += 1
            temp = self.tail
            self.tail.after = new_node
            self.tail = new_node
            self.tail.before = temp

    def pop_left(self):

        if self.head is None:
            return None

        popped_data = self.head.data
        self.size -= 1

        if self.head.after is None:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.after
            self.head.before = None

        return popped_data

    def pop(self):
        if self.tail is None:
            return None

        popped_data = self.tail.data
        self.size -= 1

        if self.tail.before is None:
            self.pop_left()

        else:
            self.tail = self.tail.before
            self.tail.after = None
            self.size -= 1
        return popped_data

    def __iter__(self):
        if self.reverse:
            self.current = self.tail

        else:
            self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            self.reverse = False
            raise StopIteration

        current_data = self.current.data
        if self.reverse:

            self.current = self.current.before
        else:
            self.current = self.current.after
        return current_data


"""
By default the linked list can be iterated in the forward way by loop.
For reverse iteration, update the reverse attibute to True.
After the end of reverse iteration, it will be set to False.
See the example of reverse iteration below:

demo_doubly_linked_list.reverse = True
    for item in demo_doubly_linked_list:
    print(item)

"""

