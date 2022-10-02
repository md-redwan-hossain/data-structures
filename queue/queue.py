# Singly linked list skeleton segment:
class Node:
    def __init__(self, data=None, after=None):
        self.data = data
        self.after = after


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    @staticmethod
    def underflow_msg():
        print("Underflow")

    def queue_size(self):
        return self.size

    def is_empty(self):
        if self.queue_size() != 0:
            return False
        else:
            return True

    def peek(self):
        if self.queue_size() != 0:
            return self.front.data

    def enqueue(self, data):
        new_node = Node(data)
        self.size += 1
        if self.front:
            temp = self.rear
            temp.after = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            delete_node = self.front
            saved_data = delete_node.data
            self.front = self.front.after
            del delete_node
            self.size -= 1
            return saved_data
        else:
            self.underflow_msg()


# Data insert segment:
# Remove the comments to use this segment:


# def inp():
#     # change data type here on demand
#     in_data = int(input("Enter data: "))
#     return in_data


# line_one = Queue()

# print("""
# 0.  Stop input
# 2.  Queue size
# 3.  Check empty or not
# 4.  Enqueue
# 5.  Deque
# 6.  Peak
# """)

# while True:
#     choice = int(input("Enter your choice: "))
#     if choice == 0:
#         break

#     elif choice == 2:
#         print(line_one.queue_size())

#     elif choice == 3:
#         if not line_one.is_empty():
#             print("Queue is not empty")
#         else:
#             print("Queue is empty")

#     elif choice == 4:
#         input_data = inp()
#         line_one.enqueue(input_data)

#     elif choice == 5:
#         if line_one.queue_size() != 0:
#             print(line_one.dequeue())
#         else:
#             line_one.underflow_msg()

#     elif choice == 6:
#         if line_one.queue_size() != 0:
#             print(line_one.peek())
