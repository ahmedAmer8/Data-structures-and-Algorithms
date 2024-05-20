class Node:
    def __init__(self, data=None):
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

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


def merge_sort(list1, list2):
    head = Node()
    curr = head
    while list1 and list2:
        if list1.data <= list2.data:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    temp = head.next
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def main():
    llist = LinkedList()
    llist.insert_at_end(0)
    llist.insert_at_end(1)
    llist.insert_at_end(4)
    llist.insert_at_end(5)
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(3)
    llist.print()
    llist2.print()
    merge_sort(llist.head, llist2.head)



if __name__ == '__main__':
    main()
