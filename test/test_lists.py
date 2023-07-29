import unittest

from src.challenges.list_impl import ArrayList

from src.answers.list_impl import LinkedList


class TestAddNumbers(unittest.TestCase):
    def test_lists_equal(self):
        arraylist = ArrayList()
        arraylist.append(10)
        arraylist.append(20)
        arraylist.append(30)

        linkedlist = LinkedList()
        linkedlist.append(10)
        linkedlist.append(20)
        linkedlist.append(30)

        for i in range(0, 3):
            self.assertEqual(linkedlist.get(i), arraylist.get(i))

    def test_arraylists_insert_error(self):
        arraylist = ArrayList()
        arraylist.append(10)
        arraylist.append(20)
        arraylist.append(30)

        with self.assertRaises(Exception):
            arraylist.insert(-1, 10)

    def test_linkedlists_equal_insert_error(self):
        arraylist = LinkedList()
        arraylist.append(10)
        arraylist.append(20)
        arraylist.append(30)

        with self.assertRaises(Exception):
            arraylist.insert(10, 0)

    def test_arraylists_get_error(self):
        arraylist = ArrayList()
        arraylist.append(10)
        arraylist.append(20)
        arraylist.append(30)

        with self.assertRaises(Exception):
            arraylist.get(-1)

    def test_linkedlists_equal_get_error(self):
        arraylist = LinkedList()
        arraylist.append(10)
        arraylist.append(20)
        arraylist.append(30)

        with self.assertRaises(Exception):
            arraylist.get(-1)


if __name__ == '__main__':
    unittest.main()
