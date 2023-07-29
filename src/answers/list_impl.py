class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, after_node_data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == after_node_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"{after_node_data} not found in the linked list.")

    def clear(self):
        self.head = None

    def get(self, index):
        if index < 0:
            raise IndexError(f"Index out of range: {index}")

        current = self.head
        counter = 0
        data = None
        while current and counter <= index:
            data = current.data
            current = current.next
            if counter == index:
                break
            else:
                counter = counter + 1

        if counter < index:
            raise IndexError(f"Index is too big: {index}")

        return data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        strs = []

        current = self.head
        while current:
            strs.append(current.data)
            current = current.next

        return str(strs)


if __name__ == '__main__':
    # this implementation does not allocate more memory during append or insert
    # however it does require iterating over the list to get values
    my_list = LinkedList()

    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    print(my_list)  # Output: [10, 20, 30]

    my_list.insert(15, 10)
    print(my_list)  # Output: [10, 15, 20, 30]

    print(my_list.get(1))  # Output: [10, 15, 20, 30]

    my_list.clear()
    print(my_list)  # Output: []

    print(my_list.is_empty())
