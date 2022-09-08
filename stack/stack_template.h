template <typename classType>
class Node {
 public:
  Node *prev;
  classType value;
  Node *next;

  Node(classType value) {
    this->prev = nullptr;
    this->value = value;
    this->next = nullptr;
  }
};

template <typename stackType>
class Stack {
  Node<stackType> *Head;
  Node<stackType> *Top;
  int count = 0;

 public:
  Stack() {
    this->Head = nullptr;
    this->Top = nullptr;
  }

  void push(stackType value) {
    Node<stackType> *pushed = new Node<stackType>(value);
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

  stackType pop() {
    stackType check;
    if (Head == nullptr) {
      return check;
    }

    Node<stackType> *delNode = Top;
    stackType savedValue = delNode->value;
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

  stackType top() {
    stackType check;
    if (Head == nullptr) {
      return check;
    }
    else
      return Top->value;
  }

  int size() {
    return count;
  }
};
