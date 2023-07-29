def simple_hash(key: str):
    return len(key) % 5


class HashStorage:
    storage = {}

    def add_value(self, value: str):
        hashed_key = simple_hash(value)

        self.storage[hashed_key] = value


if __name__ == '__main__':
    values = ["apple", "banana", "grape", "lemon", "orange", "pear", "kiwi", "watermelon"]
    storage = HashStorage()
    for value in values:
        storage.add_value(value)
