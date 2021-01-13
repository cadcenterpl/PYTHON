from KM_zad1_1 import LinkedList
from typing import Any

class Queue:
    _storage: LinkedList()

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self):
        sh = self._storage.head
        val: str = ''
        while sh.next != None: 
            val += str(sh.value) + ", "
            sh = sh.next
        val += str(sh.value)
        return val

    def __len__(self):
        return len(self._storage)

    def enqueue(self, element: Any):
        self._storage.append(element)

    def dequeue(self):
        return self._storage.pop()

    def peek(self):
        return self._storage.head.value


# Pusta kolejka
queue = Queue()

# len test 1
assert len(queue) == 0

# dodanie do kolejki 
queue.enqueue("klient1")
queue.enqueue("klient2")
queue.enqueue("klient3")

# test FIFO kolejności
assert str(queue) == 'klient1, klient2, klient3'

# test FIFO wyjścia
client_first = queue.dequeue()

assert client_first == 'klient1'

# test kolejki po wyjściu
assert str(queue) == 'klient2, klient3'

# len test 2
assert len(queue) == 2
#print(queue)
