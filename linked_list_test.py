import unittest
from linked_list import Linked_List

#todo def deleteduplicates
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = Linked_List()

    def tearDown(self):
        pass

    def test_count(self):
        count = self.linked_list.count()
        self.assertEqual(count, 0)
        self.linked_list.insert(1)
        count = self.linked_list.count()
        self.assertEqual(count, 1)
        self.linked_list.insert(1)
        count = self.linked_list.count()
        self.assertEqual(count, 2)

    def test_get(self):
        with self.assertRaisesRegex(Exception, 'The list is empty'):
            self.linked_list.get(0)
        self.linked_list.insert(1)
        get = self.linked_list.get(0)
        self.assertEqual(get, 1)
        self.linked_list.insert(1)
        get = self.linked_list.get(1)
        self.assertEqual(get, 1)
        with self.assertRaisesRegex(Exception, 'Your list does not have that index.'):
            self.linked_list.get(3)

    def test_find(self):
        with self.assertRaisesRegex(Exception, 'The list is empty'):
            self.linked_list.find(0)
        self.linked_list.insert(1)
        find = self.linked_list.find(1)
        self.assertEqual(find, 0)
        self.linked_list.insert(2)
        find = self.linked_list.find(2)
        self.assertEqual(find, 1)

    def test_remove_by_index(self):
        with self.assertRaisesRegex(Exception, "The list is empty, can't remove any index."):
            self.linked_list.remove_by_index(0)
        self.linked_list.insert(1)
        with self.assertRaisesRegex(Exception, 'Your list do not contained that index number'):
            self.linked_list.remove_by_index(5)
        remove_by_index = self.linked_list.remove_by_index(0)
        self.assertEqual(remove_by_index, None)
        self.linked_list.insert(1)
        self.linked_list.insert(1)
        self.linked_list.remove_by_index(0)
        self.assertEqual(self.linked_list.get(0), 1)

    def test_replace_by_index(self):
        with self.assertRaisesRegex(Exception, 'The list is empty, can only insert to index 0'):
            self.linked_list.replace_by_index(0, 1)
        self.linked_list.insert(1)
        with self.assertRaisesRegex(Exception, 'Your list do not contained that index number'):
            self.linked_list.replace_by_index(5, 2)
        with self.assertRaisesRegex(Exception, 'Your list do not contained that index number'):
            self.linked_list.replace_by_index(2, 2)
        self.linked_list.replace_by_index(2, 0)
        self.assertEqual(self.linked_list.find(2), 0)
        self.linked_list.insert(1)
        self.assertEqual(self.linked_list.find(1), 1)

    def test_insert_by_index(self):
        with self.assertRaisesRegex(Exception, 'Your list do not contained that index number'):
            self.linked_list.replace_by_index(0, 0)
        with self.assertRaisesRegex(Exception, 'The list is empty, can only insert to index 0'):
            self.linked_list.replace_by_index(1, 1)
        self.linked_list.insert(1)
        with self.assertRaisesRegex(Exception, 'Your list do not contained that index number'):
            self.linked_list.replace_by_index(0, 4)
        self.linked_list.replace_by_index(2, 0)
        self.assertEqual(self.linked_list.find(2), 0)
        self.linked_list.insert(1)
        self.linked_list.replace_by_index(1, 0)
        self.assertEqual(self.linked_list.find(1), 0)

    def test_insert(self):
        self.linked_list.insert(1)
        self.assertEqual(self.linked_list.get(0), 1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual(self.linked_list.get(2), 3)

    def test_delete_duplicates(self):
        pass


if __name__ == '__main__':
    unittest.main()
