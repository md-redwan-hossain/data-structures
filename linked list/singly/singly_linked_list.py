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

    def list_size(self):
        return self.size

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

    def insert_before_position(self, target_position, data):
        if self.head and not self.head.after:
            self.insert_at_head(data)

        elif self.head and self.head.after:
            new_node = Node(data)
            if target_position <= self.list_size():
                target_position -= 1
                destination = 0
                temp = self.head
                while temp:
                    destination += 1
                    if destination == target_position:
                        break
                    temp = temp.after

                saved = temp.after
                temp.after = new_node
                new_node.after = saved
                self.plus_size()
        else:
            self.empty_msg()

    def insert_after_position(self, target_position, data):
        if self.head:
            new_node = Node(data)
            if target_position <= self.list_size():
                destination = 0
                temp = self.head
                while temp:
                    destination += 1
                    if destination == target_position:
                        break
                    temp = temp.after

                saved = temp.after
                temp.after = new_node
                new_node.after = saved
                self.plus_size()
        else:
            self.empty_msg()

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

    def mid_of_list(self):
        if self.head:
            slow, fast = self.head, self.head
            while (fast and fast.after):
                fast = fast.after.after
                slow = slow.after
            return slow.data
        else:
            self.empty_msg()

    def print_list(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.after
        else:
            self.empty_msg()


# # Data insert segment:
# # Remove the comments to use this segment:


# def inp():
#     # change data type here on demand
#     in_data = int(input("Enter data: "))
#     return in_data


# def inp_target():
#     # change data type here on demand
#     in_target = int(input("Enter target location: "))
#     in_data = int(input("Enter data: "))
#     return in_target, in_data


# list_one = LinkedList()

# print("""
# 0. Stop input
# 1. Print singly linked list
# 2. List size
# 3. Mid of linked list
# 4. Insert at head
# 5. Insert at tail
# 6. Insert before position
# 7. Insert after position
# 8. Delete at head
# 9. Delete at tail
# """)

# while True:
#     choice = int(input("Enter your choice: "))
#     if choice == 0:
#         break

#     elif choice == 1:
#         list_one.print_list()

#     elif choice == 2:
#         print(list_one.list_size())

#     elif choice == 3:
#         print(list_one.mid_of_list())

#     elif choice == 4:
#         input_data = inp()
#         list_one.insert_at_head(input_data)

#     elif choice == 5:
#         input_data = inp()
#         list_one.insert_at_tail(input_data)

#     elif choice == 6:
#         verify = list_one.list_size()
#         if verify != 0:
#             print(f"You have {verify} nodes.")
#             input_data_and_target = inp_target()
#             list_one.insert_before_position(
#                 input_data_and_target[0], input_data_and_target[1])
#         else:
#             list_one.empty_msg()

#     elif choice == 7:
#         verify = list_one.list_size()
#         if verify != 0:
#             print(f"You have {verify} nodes.")
#             input_data_and_target = inp_target()
#             list_one.insert_after_position(
#                 input_data_and_target[0], input_data_and_target[1])
#         else:
#             list_one.empty_msg()

#     elif choice == 8:
#         list_one.delete_at_head()

#     elif choice == 9:
#         list_one.delete_at_tail()
