class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
        else:
            new_node = Node(data)
            current_node = self.head
            position = 0
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index out of range")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def update_node(self, data, index):
        if self.head is None and index == 0:
            self.head = Node(data)
            return
        position = 0
        current_node = self.head
        while position != index and current_node:
            current_node = current_node.next
            position += 1
        if current_node is None:
            print("There is no such an index in the list")
            return
        current_node.data = data

    def remove_node(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        position = 0
        current_node = self.head
        while position + 1 != index and current_node.next:
            current_node = current_node.next
            position += 1
        if current_node.next is None:
            print("index out of range")
            return
        current_node.next = current_node.next.next

    def remove_last_node(self):
        self.remove_node(self.size()-1)

    def size(self):
        if self.head is None:
            return 0
        size = 1
        current_node = self.head.next
        while current_node:
            current_node = current_node.next
            size += 1
        return size

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next




def main():
    llist = LinkedList()

    # add nodes to the linked list
    llist.insert_at_end('a')
    llist.insert_at_end('b')
    llist.insert_at_begin('c')
    llist.insert_at_end('d')
    llist.insert_at_index('g', 2)

    # print the linked list
    print("Node Data")
    llist.print()

    # remove a nodes from the linked list
    print("\nRemove First Node")
    llist.remove_node(0)
    print("Remove Last Node")
    llist.remove_last_node()
    print("Remove Node at Index 1")
    llist.remove_node(1)

    # print the linked list again
    print("\nLinked list after removing a node:")
    llist.print()

    print("\nUpdate node Value")
    llist.update_node('z', 0)
    llist.print()

    print("\nSize of linked list :", end=" ")
    print(llist.size())


if __name__ == '__main__':
    main()

