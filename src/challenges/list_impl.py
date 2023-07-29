class ArrayList:
    def __init__(self):
        self._data = []  # Internal list to store elements. do not depend on python list functiions
        self._size = 0  # Current number of elements in the ArrayList

    def append(self, value):
        # assign new memory values
        new_data = [0 for _ in range(self._size + 1)]

        # populate with the existing values
        for i in range(0, self._size):
            new_data[i] = self._data[i]

        # add new value
        new_data[self._size] = value

        self._data = new_data
        self._size = len(new_data)

    def insert(self, index, value):
        if index > self._size or index < 0:
            raise Exception(f"Invalid index: {index}")

        # assign new memory values
        new_data = [0 for _ in range(self._size + 1)]

        # populate the head
        for i in range(0, index):
            new_data[i] = self._data[i]

        # set the new value
        new_data[index] = value

        # populate the tail
        for i in range(index, self._size):
            new_data[i + 1] = self._data[i]

        self._data = new_data
        self._size = len(new_data)

    def clear(self):
        self._data.clear()
        self._size = 0

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of range: {index}")

        return self._data[index]

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    # advantage of this impl: can get elements by index
    # what are the disadvantages? what other list implementation would solve them?
    my_list = ArrayList()

    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    print(my_list)  # Output: [10, 20, 30]

    my_list.insert(1, 15)
    print(my_list)  # Output: [10, 15, 20, 30]

    my_list.clear()
    print(my_list)  # Output: []

    print(my_list.is_empty())
