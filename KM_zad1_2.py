from KM_zad1_1 import LinkedList
from typing import Any

class Stack:
    _storage: LinkedList()

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self):
        val = ""
        sh = self._storage.head
        while sh.next != None:
            val += str(sh.value) + " \n"
            sh = sh.next
        val += str(sh.value)
        return val

    def __len__(self):
        return len(self._storage)

    def push(self, element: Any):
        self._storage.push(element)

    def pop(self):
        return self._storage.pop()

# Pusty stos
stack = Stack()

# len test 1
assert len(stack) == 0

# Push
stack.push(3)
stack.push(10)
stack.push(1)

# len test 2
assert len(stack) == 3

# zdjęcie ze szczytu i pop test
top_value = stack.pop()
assert top_value == 1

# len test 3
assert len(stack) == 2
# print(stack)