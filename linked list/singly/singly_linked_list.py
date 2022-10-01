# Singly linked list skeleton segment:
class Node:
    def __init__(self, data=None, after=None):
        self.data = data
        self.after = after


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def empty_msg(self):
        print("list is empty")

    def plus_size(self):
        self.size += 1

    def minus_size(self):
        self.size -= 1

    def insert_at_head(self, data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.after = temp
        self.plus_size()

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head:
            self.plus_size()
            temp = self.head
            while temp.after:
                temp = temp.after
            temp.after = new_node
        else:
            self.insert_at_head(data)

    def delete_at_head(self):
        if self.head:
            delete_node = self.head
            self.head = self.head.after
            del delete_node
            self.minus_size()
        else:
            self.empty_msg()

    def delete_at_tail(self):
        if self.head.after:
            temp = self.head
            while temp.after.after:
                temp = temp.after
            delete_node = temp.after
            del delete_node
            temp.after = None
            self.minus_size()
        elif self.head:
            self.delete_at_head()
        else:
            self.empty_msg()

    def list_size(self):
        return self.size

    def print_list(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.after
        else:
            self.empty_msg()


# Data insert segment:
# Remove the triple quotes(block comment) to use this segment:

"""
def inp():
    # change data type here on demand
    input_data = int(input("Enter data: "))
    return input_data


list_one = LinkedList()

print("0. Stop input", "1. Print singly linked list", "2. List size",
      "3. Insert at head", "4. Insert at tail", "7. Delete at head", "8. Delete at tail", sep="\n")


while True:
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break

    elif choice == 1:
        list_one.print_list()

    elif choice == 2:
        print(list_one.list_size())

    elif choice == 3:
        input_data = inp()
        list_one.insert_at_head(input_data)

    elif choice == 4:
        input_data = inp()
        list_one.insert_at_tail(input_data)

    elif choice == 7:
        list_one.delete_at_head()

    elif choice == 8:
        list_one.delete_at_tail()
"""
