"""Module: Container """
from container import Container


class Stack(Container):
    """Subclass of Container with LIFO implementation"""

    def __init__(self):
        # Initialization is done at superclass
        super(Stack, self).__init__()

    def pop(self):
        """Pop off the first element"""
        assert not self.is_empty()
        return self._items.pop(self.size() - 1)

    def peek(self):
        """Return the first element of the list without deleting it"""
        assert not self.is_empty()
        return self._items[self.size() - 1]
