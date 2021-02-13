
class Container:

    def __init__(self):
        self._items = []

    def size(self):
        # Return number of elements in self._items
        return len(self._items)

    def is_empty(self):
        # Check if self._items is empty
        if not self._items:
            return True
        return False

    def push(self, item):
        # Add item to end of self._items
        self._items.append(item)

    def pop(self):
        # Pop off the correct element of self._items, and return it
        # This method differs between subclasses, hence is not
        # implemented in the superclass
        raise NotImplementedError

    def peek(self):
        # Return the top element without removing it
        # This method differs between subclasses, hence is not
        # implemented in the superclass
        raise NotImplementedError

