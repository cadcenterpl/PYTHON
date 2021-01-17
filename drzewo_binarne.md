## DRZEWO BINARNE + WIZUALIZACJA (PYTHON)

![Image](https://github.com/cadcenterpl/PYTHON/blob/master/ssbtpy.png)

- Klasy i Metody
```markdown
from typing import Any
import queue

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value 

    def is_leaf(self) -> bool:
        return not (self.left_child or self.right_child)
    
    def add_left_child(self, value: Any):
        tnode = BinaryNode(value)
        if self.left_child is None:
            self.left_child = tnode
        else:
            return False
    
    def add_right_child(self, value: Any):
        tnode = BinaryNode(value)
        if self.right_child is None:
            self.right_child = tnode
        else:
            return False

    def __str__(self)-> str:
        return str(self.value)
   
class BinaryTree:
    root: BinaryNode

    def __init__(self, korzen: BinaryNode):
        korz = BinaryNode(korzen)
        self.root = korz

```
- Funkcje
```markdown

def traverse_in_order(root, lista):
    if root:
        traverse_in_order(root.left_child, lista)
        lista.append(root.value)
        traverse_in_order(root.right_child, lista)

def traverse_post_order(root, lista):
    if root:
        traverse_post_order(root.left_child, lista)
        traverse_post_order(root.right_child, lista)
        lista.append(root.value)

def traverse_pre_order(root, lista):
    if root:
        lista.append(root.value)
        traverse_pre_order(root.left_child, lista)
        traverse_pre_order(root.right_child, lista)

def level_order(root, lista):
    Q = queue.Queue()
    Q.put(root)
    while Q.empty() != True:
        root = Q.get()
        lista.append(root.value)
        if root.left_child != None:
            Q.put(root.left_child)
        if root.right_child != None:
            Q.put(root.right_child)

def list_creator(funkcja, drzewo):
    lista = []
    funkcja(drzewo, lista)
    return lista
```
- Budowanie drzewa
```markdown
tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)
```
- Testy
```markdown
assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
assert str(tree.root.left_child.left_child) == '1'
assert list_creator(traverse_in_order, tree.root) == [1, 9, 3, 10, 4, 2, 6]
assert list_creator(traverse_post_order, tree.root) == [1, 3, 9, 4, 6, 2, 10]
assert list_creator(traverse_pre_order, tree.root) == [10, 9, 1, 3, 2, 4, 6]
assert list_creator(level_order,tree.root) == [10, 9, 2, 1, 3, 4, 6]
```
- Wizualizacja Turtle

```markdown
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if value == 'null' else BinaryNode(int(value))
             for value in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left_child  = kids.pop()
            if kids: node.right_child = kids.pop()
    return root

def show(root):
    def height(root):
        return 1 + max(height(root.left_child), height(root.right_child)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-40)
            t.write(node.value, align='center', font=('Arial', 24, 'normal'))
            draw(node.left_child, x-dx, y-100, dx/2)
            jumpto(x, y-40)
            draw(node.right_child, x+dx, y-100, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(4); turtle.delay(0)
    h = height(root)
    jumpto(0,120)
    t.write('Drzewo Binarne AiSD Lab5', align='center', font=('Arial', 24, 'bold'))
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    show(deserialize(str(list_creator(level_order,tree.root))))
```
