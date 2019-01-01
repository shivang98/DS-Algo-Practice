class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_beginning(self, data):
        self.size += 1
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_end(self, data):
        self.size += 1
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert_at(self, data, pos):
        node = Node(data)

        if pos == 0:
            self.insert_beginning(data)
            return
        elif self.size <= pos:
            self.insert_end(data)
            return

        self.size += 1
        current = self.head
        pos_count = 0
        while(pos_count < pos):
            current = current.next
            pos_count += 1
        node.next = current
        node.prev = current.prev
        current.prev.next = node
        current.prev = node

    def display(self):
        current = self.head
        if current == None:
            print("Empty Linkedlist")
            return
        while(current != None):
            print(current.data)
            current = current.next

    def display_rev(self):
        current = self.tail
        if self.tail == None:
            print("Empty Linkedlist")
        while current != None:
            print(current.data)
            current = current.prev

if __name__ == '__main__':

    # dll = Doubly_linked_list()
    # dll.insert_beginning(1)
    # dll.insert_beginning(2)
    # dll.insert_beginning(3)
    # dll.insert_beginning(4)

    # dll.insert_end(1)
    # dll.insert_end(2)
    # dll.insert_end(3)
    # dll.insert_end(4)

    # dll.insert_at(10,4)

    # dll.display()
