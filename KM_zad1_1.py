from typing import Any

#1 Klasa Node
class Node (object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

#2 Klasa Lista
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

#3 Push
    def push(self, value):
        node = Node(value)
        node.next = self.head 
        self.head = node

#4 Append 
    def append(self,value):
        node = Node(value)
        sh = self.head
        if not sh:
            self.head = node
        else:
            while sh.next != None:
                sh = sh.next
            sh.next = node

#5 Node
    def node(self, at: int) -> Node:
        sh = self.head
        for i in range (at):
            sh = sh.next
        return sh

#6 Insert
    def insert(self, value: Any, after: Node):
        node = Node(value)
        node.next = after.next
        after.next = node

#7 Pop
    def pop(self)->Any:
        shF = self.node(0)
        sh = self.head
        self.head = sh.next
        sh = None
        return shF.value

#8' Tail
    def tail_config(self)->Node:
        sh = self.head
        while sh.next is not None:
            sh=sh.next
        self.tail = sh
        return self.tail

#8 LER
    def remove_last(self)->Any:
        st = self.tail_config()
        sh = self.head
        while sh.next != st:
            sh = sh.next
        self.tail = sh
        self.tail.next = None
        return st.value

#9 RE
    def remove(self, after: Node)->Any:
        sh = self.head
        while sh.next != None and sh.next is after:
            sh = sh.next
        if (sh.next == None):
            sh.next = None
        else:
            sh.next = sh.next.next
    
#Wyświetlanie / Sprawdzanie
    def __str__(self):
        sh = self.head
        val: str = ''
        while sh.next != None: 
            val += str(sh.value) + " -> "
            sh = sh.next
        val += str(sh.value)
        return val
#len
    def __len__(self):
        sh = self.head
        l: int = 0
        while sh != None:
            l += 1
            sh = sh.next
        return l

#10 
def __print__(listaa: LinkedList):
    lh = listaa.head
    val: str = ''
    while lh.next != None: 
        val += str(lh.value) + " -> "
        lh = lh.next
    val += str(lh.value)
    return val

def len(listaa: LinkedList):
    lh = listaa.head
    l: int = 0
    while lh != None:
        l += 1
        lh = lh.next
    return l

#Pusta lista
list_ = LinkedList()
assert list_.head == None
# Push
for i in range (1,-1,-1): list_.push(i)
assert str(list_) == "0 -> 1"
# Append
for i in range (2): list_.append(i+9)
assert str(list_) == "0 -> 1 -> 9 -> 10"
# Node
assert str(list_.node(2).value) == "9"
# Insert
list_.insert(5, list_.node(1))
assert str(list_) == "0 -> 1 -> 5 -> 9 -> 10"
# POP
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
assert str(list_) == "1 -> 5 -> 9 -> 10"
# LER
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'
# ER
second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'
#print(list_)
#Wyświetlenie obiektu lista [0,1]
lista1 = LinkedList()
for i in range (2): lista1.append(i)
#print(lista1)
#Funkcja zwracająca długość listy
assert str(len(lista1)) == "2"