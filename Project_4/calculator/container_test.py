"""Module: Container """
import unittest

from queue import Queue
from stack import Stack


class TestContainers(unittest.TestCase):
    """TestCase for 'Container' and its subclasses."""

    def test_push(self):
        """Testing push() in 'Queue' and 'Stack'"""
        test_queue = Queue()
        test_stack = Stack()

        queue_size_before = test_queue.size()
        stack_size_before = test_stack.size()
        test_queue.push(0)
        self.assertTrue(
            test_queue.size() == queue_size_before + 1,
            "Method push failed on 'Queue'")
        test_stack.push(0)
        self.assertTrue(
            test_stack.size() == stack_size_before + 1,
            "Method push failed on 'Stack'")

    def test_size(self):
        """Testing size() in 'Queue' and  'Stack'."""
        test_queue = Queue()
        test_stack = Stack()

        self.assertEqual(
            0,
            test_queue.size(),
            "Method size() failed on 'Queue'")
        test_queue.push("test")
        test_queue.push(0)
        self.assertEqual(
            2,
            test_queue.size(),
            "Method size() failed on 'Queue'")
        self.assertEqual(
            0,
            test_stack.size(),
            "Method size() failed on 'Stack'")
        test_stack.push("test")
        test_stack.push(0)
        self.assertEqual(
            2,
            test_stack.size(),
            "Method size() failed on 'Stack'")

    def test_is_empty(self):
        """Testing is_empty() on 'Stack' and 'Queue'."""
        test_queue = Queue()
        test_stack = Stack()

        self.assertTrue(
            test_queue.is_empty(),
            "Method is_empty() failed on 'Queue'")
        test_queue.push(1)
        self.assertFalse(
            test_queue.is_empty(),
            "Method is_empty() failed on 'Queue'")

        self.assertTrue(
            test_stack.is_empty(),
            "Method is_empty() failed on 'Stack'")
        test_stack.push(1)
        self.assertFalse(
            test_stack.is_empty(),
            "Method is_empty() failed on 'Stack'")

    def test_pop_and_peek_queue(self):
        """Testing pop() and peek() on 'Queue'"""
        test_queue = Queue()
        test_stack = Stack()

        for i in range(1, 11):
            test_queue.push(i)
        for i in range(1, 11):
            self.assertTrue(
                test_queue.peek() == i,
                "Method peek() failen on 'Queue'")
            item_to_pop = test_queue.peek()
            print(item_to_pop)
            self.assertTrue(
                test_queue.pop() == i,
                "Method pop() failen on 'Queue'")
        self.assertTrue(test_queue.is_empty(), "'Queue' should be empty")

        for i in range(1, 11):
            test_stack.push(i)
        for i in range(1, 11):
            self.assertTrue(
                test_stack.peek() == 11 - i,
                "Method peek() failen on 'Stack'")
            item_to_pop = test_stack.peek()
            print(item_to_pop)
            self.assertTrue(
                test_stack.pop() == 11 - i,
                "Method pop() failen on 'Stack'")
        self.assertTrue(test_stack.is_empty(), "'Stack' should be empty")


if __name__ == '__main__':
    unittest.main()
