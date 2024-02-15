from unittest import TestCase
from linked_list import LinkedList

class TestRemoveLinkedList(TestCase):

    def test_01_remove_first(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_first)

    def test_02_remove_first(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        l.remove_first()
        self.assertEqual(0, len(l), 'элемент не удалён')

    def test_03_remove_last(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_last)

    def test_04_remove_last(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        l.remove_last()
        self.assertEqual(0, len(l), 'элемент не удалён')

    def test_05_remove_at(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_at, 0)

    def test_06_remove_at(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_at, -1)

    def test_07_remove_at(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        l.remove_at(0)
        self.assertEqual(0, len(l), 'элемент не удалён')

    def test_08_remove_first_value(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_first_value, 0)

    def test_09_remove_first_value(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        self.assertRaises(ValueError, l.remove_first_value, 0)

    def test_10_remove_first_value(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        l.remove_first_value(1)
        self.assertEqual(0, len(l), 'элемент не удалён')

    def test_11_remove_last_value(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.remove_last_value, 0)

    def test_12_remove_last_value(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        self.assertRaises(ValueError, l.remove_last_value, 0)

    def test_13_remove_last_value(self):
        l = LinkedList()
        l.append_begin(1)
        self.assertEqual(1, len(l), 'элемент не добавлен')
        l.remove_last_value(1)
        self.assertEqual(0, len(l), 'элемент не удалён')