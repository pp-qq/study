class ListNoed:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = None

    # Iteratorを定義
    def __iter__(self):
        self.current = self.head
        return self

    # Iterateする
    def __next__(self):
        if self.current:
            value = self.current.value
            self.current = self.current.next
            return value
        else:
            raise StopIteration


# LinkedListを作成
head = ListNoed(1)
head.next = ListNoed(2)
head.next.next = ListNoed(3)
myList = LinkedList(head)

# Iterateする
for value in myList:
    print(value)
