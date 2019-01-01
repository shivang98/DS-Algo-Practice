class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.size = self.size + 1

    def size1(self):
        return self.size

    def display(self):
        current = self.head
        if current == None:
            print("Empty Linkedlist")
            return
        while(current != None):
            print(current.data, end = "->")
            current = current.next
        print("None")

if __name__ == '__main__':

    ll = Linked_List()
    ll.insert_at_head(1)
    ll.insert_at_head(2)
    ll.insert_at_head(3)
    ll.display()
