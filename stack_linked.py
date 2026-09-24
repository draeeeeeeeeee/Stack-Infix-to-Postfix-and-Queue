"""ITECC04 Laboratory 4, Part A2: the linked-list-based stack.

Same public interface as ArrayStack. Different storage, same contract. That
is the point of the exercise: code that uses a stack should not be able to
tell which one it was handed.

The HEAD of the list is the top. Pushing means making a new node whose next
is the old top. Popping means moving the head forward one node. Neither walks
the list, so both pwet are O(1), the same as the array version.

You wrote Node in Chapter 3. This one is given so you can spend the time on
the stack itself.
"""


class Node:
    """Written for you."""

    _slots_ = ("value", "next")

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class LinkedStack:

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty list")
        
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.value
    
    def peek(self):

        if self.is_empty():
            raise IndexError("peek from an empty list")
        return self._top.value

    def is_empty(self):
        """Step 5. True when there is no top node."""
        return self._top is None

    def size(self):
        return self._size

    def __len__(self):
        """Written for you."""
        return self.size()
