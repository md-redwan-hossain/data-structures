class Node {
 public:
  Node *prev;
  int value;
  Node *next;

  Node(int value) {
    this->prev = nullptr;
    this->value = value;
    this->next = nullptr;
  }
};

class Stack {
  Node *Head;
  Node *Top;
  int count = 0;

 public:
  Stack() {
    this->Head = nullptr;
    this->Top = nullptr;
  }

  void push(int value) {
    Node *pushed = new Node(value);
    if (Head == nullptr) {
      Head = Top = pushed;
      ++count;
      return;
    }
    Top->next = pushed;
    pushed->prev = Top;
    Top = pushed;
    ++count;
  }

  int pop() {
    if (Head == nullptr) {
      return -1;
    }

    Node *delNode = Top;
    int savedValue = delNode->value;

    if (Head == Top) {
      Head = Top = nullptr;
    }
    else {
      Top = delNode->prev;
      Top->next = nullptr;
    }

    delete delNode;
    --count;
    return savedValue;
  }

  bool isEmpty() {
    if (Head == nullptr)
      return true;
    else
      return false;
  }

  int top() {
    if (Head == nullptr) {
      return -1;
    }
    else
      return Top->value;
  }

  int size() {
    return count;
  }
};
