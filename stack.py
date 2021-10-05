from linkedlist import LinkedList


class Stack:
    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def __repr__(self) -> str:
        nodes = [str(node.data) for node in self.linked_list]
        return " ".join(nodes)

    def push(self, data):
        self.linked_list.insert_at_head(data)

    def pop(self):
        try:
            data = self.peek()
            self.linked_list.remove_at_head()
            return data
        except:
            raise Exception("Stack is empty")

    def peek(self):
        return self.linked_list.head.data

    def size(self):
        return self.linked_list.size


def main():

    brackets = {'o': '([{', 'c': ')]}'}

    seq = input("Input bracket sequence: ")
    stack = Stack()

    for b in seq:
        if b in brackets['o']:
            stack.push(b)

        elif b in brackets['c']:
            if stack.peek() == brackets['o'][brackets['c'].index(b)]:
                stack.pop()
            else:
                break
        else:
            raise Exception(f"Invalid token {b}")

    if stack.size() > 0:
        print('Invalid bracket sequence.')
    else:
        print('Valid bracket Squence')


if __name__ == '__main__':
    main()
