"""Module: Container """
from container import Container


class Queue(Container):
    """Subclass of Container with FIFO implementation"""

    def __init__(self):
        """Initialization is done at superclass"""
        super(Queue, self).__init__()

    def pop(self):
        """Pop off the first element"""
        assert not self.is_empty()
        return self._items.pop(0)

    def peek(self):
        """Return the first element of the list without deleting it"""
        assert not self.is_empty()
        return self._items[0]
