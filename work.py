# from __future__ import annotations
# from typing import Any
#
# class Node(object):
#     def __init__(self, data: Any, next_node: Node = None):
#         self.data = data
#         self.next = next_node
#
#
# class LinkedList(object):
#     def __init__(self, head=None) -> None:
#         self.head = head
#
#     def append(self, data: Any) -> None:
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#     def insert (self, data: Any) -> None:
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def print(self) -> None:
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next
#     def remove(self, data: Any) -> None:
#         import gc
#         current_node = self.head
#         if current_node and current_node.data == data:
#             self.head = current_node.next
#             # current_node = Node
#             gc.collect()
#             return
#         previous_node = None
#         while current_node and current_node.data != data:
#             previous_node = current_node
#             current_node = current_node.next
#
#         if current_node is None:
#             return
#         previous_node.next = current_node.next
#         current_node = None
#
#
#
#
#
#
#
#
#     def reverse_iterative(self) -> None:
#         previous_node = None
#         current_node = self.head
#         while current_node:
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#
#         self.head = previous_node
#     def reverse_recursive(self) -> None:
#         def _reverse_recursive(current_node: None, previous_node: Node):
#             if not current_node:
#                 return previous_node
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#             return _reverse_recursive(current_node, previous_node)
#         self.head = _reverse_recursive(self.head, None)
#
#     def reverse_even(self) -> None:
#         def _reverse_even(head: Node, previous_node: Node):
#             if head is None:
#                 return None
#             current_node = head
#
#         while current_node and current_node.data % 2 == 0:
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#
#
#         if current_node != head:
#             head.next = current_node
#             _reverse_even(current_node,None)
#
#             return previous_node
#         else:
#             head.next = _reverse_even(head.next, head)
#             return head
#
#     self.head = _reverse_even(self.head, None)
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     l = LinkedList()
#     l.append(1)
#     l.append(2)
#     l.append(3)
#     l.append(0)
#     l.print()
#     # l.remove(2)
#     print("ffffff")
#     # l.print()
#     l.reverse_iterative()
#     l.print()

# from __future__ import annotations
# from typing import Any, Optional
#
# class Node(object):
#     def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
#         self.data = data
#         self.next = next_node
#         self.prev = prev_node
#
#
# class DoublyLinkedList(object):
#     def __init__(self, head: Node = None) -> None:
#         self.head = head
#
#     def append(self, data: Any) -> None:
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#
#         while current_node.next:
#             current_node = current_node.next
#             current_node.next = new_node
#             new_node.prev = current_node
#
#
#
#     def insert(self, data: Any) -> None:
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         self.head.prev = new_node
#         new_node.next = self.head
#         self.head = new_node
#
#     def print(self) -> None:
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current = current_node.next
#
#     def remove(self, data: Any) -> Node:
#         current_node = self.head
#         if current_node and current_node.data == data:
#             if current_node.next is None:
#                 current_node = None
#                 self.head = None
#                 return
#             else:
#                 next_node = current_node.next
#
#                 next_node.prev = None
#
#                 current_node = None
#                 self.head = next_node
#                 return
#         while current_node and current_node.data != data:
#             current_node = current_node.next
#
#         if current_node is None:
#             return
#         if current_node.next is None:
#             prev = current_node.prev
#             prev.next = None
#             current_node = None
#             return
#         else:
#             next_node = current_node.next
#             prev_node = current_node.prev
#             prev_node.next = next_node
#             next_node.prev = prev_node
#             current_node = None
#             return




# if __name__ == '__main__':
#     d = DoublyLinkedList()
#     d.append(1)
#     d.append(2)
#     d.append(3)
#     d.insert(0)
#     # d.print()



# import hashlib
# from typing import Any
#
#
# class HashTable(object):
#     def __init__(self, size=10) -> None:
#         self.size = size
#         self.table = [[] for _ in range(self.size)]
#
#     def hash(self, key) -> int:
#         return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size
#
#     def add(self, key, value) -> None:
#         index = self.hash(key)
#         for data in self.table[index]:
#             if data[0] == key:
#                 data[1] = value
#                 break
#             else:
#
#                 self.table[index].append([key, value])
#
#
#     def print(self) -> None:
#         for index in range(self.size):
#             print(index, end=' ')
#             for data in self.table[index]:
#                 print('-->', end=' ')
#                 print(data, end=' ')
#
#             print()
#     def get(self, key) -> Any:
#         index = self.hash(key)
#         for data in self.table[index]:
#             if data[0] == key:
#                 return data[1]
#     def __setitem__(self, key, value) -> None:
#
#         self.add(key, value)
#     def __getitem__(self, key) -> Any:
#         return self.get(key)
#
#
#
#
#
# if __name__ == '__main__':
#
#     hash_table = HashTable()
#     hash_table.add('car', 'Tesla')
#     hash_table.add('car', 'Tesla')
#     hash_table.add('car', 'Tesla')
#     hash_table.add('sns', 'yotube')
#
#     print(hash_table.table)
#     hash_table.print()



# from typing import List, Tuple, Optional
#
#
# def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
#     cache = set()
#     for num in numbers:
#         val = target - num
#         if val in cache:
#             return val, num
#         cache.add(num)
#
#
# def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
#
#     sum_numbers = sum(numbers)
#
#
#     half_sum, remainder = divmod(sum_numbers, 2)
#     if remainder != 0:
#         return
#     cache = set()
#     for num in numbers:
#         cache.add(num)
#         val = half_sum - num
#         if val in cache:
#             return val, num
# if __name__ == '__main__':
#     l = [11, 2, 4, 1]
#     l = [11, 2,1]
#
#     t = 12
#     print(get_pair(l, t))
#
#     l = [1,3,4,1, 11]
#     print(get_pair_half_sum())


# from typing import Any
#
#
#
# class Stack(object):
#     def __init__(self) -> None:
#         self.stack = []
#     def push(self, data) -> None:
#         self.stack.append(data)
#     def pop(self) -> Any:
#         if self.stack:
#             return self.stack.pop()
#
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.stack)
#     stack.push(1)
#     print(stack.stack)
#     print(stack.push(2))
#     # print(stack.pop)

# def validatate_format(chars: str) -> bool:
#     lookup = {'{': '}', '[': ']', '(': ')'}
#     stack = []
#     for char in chars:
#         if char in lookup.keys():
#             stack.append(lookup[chars])
#         if char in lookup.values():
#             if not stack:
#                 return False
#             if char != stack.pop():
#                 return False
#
#
#     if stack:
#         return  False
#     return True
#
# if __name__ == '__main__':

# from typing import Any
# from collections import deque
#
# class Queue(object):
#     def __init__(self) -> None:
#         self.queue = []
#     def enqueue(self, data: Any) -> None:
#         self.queue.append(data)
#     def dequeue(self) -> Any:
#         if self.queue:
#             return self.queue.pop(0)
#
# if __name__ == '__main__':
#     q = deque()
#     q.append(1)
#     q.append(2)
#     q.append(3)
#     q.append(4)
#     print(q)
# print


    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(1)
    # q.enqueue(1)
    # print(q.queue)
    # print(q.dequeue())
    # print(q.dequeue())



from collections import deque


# from typing import Any



# def reverse(queue: deque) -> deque:
#     new_queue = deque()
#     while queue:
#         new_queue.append(queue.pop())
#     [queue.append(d) for d in new_queue]
#     # return new_queue
#
#
#
# if __name__ == '__main__':
#     q = deque()
#     q.append(1)
#     q.append(2)
#     q.append(3)
#     q.append(4)
#     print(q)
#     #
#     # q = reverse(q)
#     # print(q)
#     reverse(q)
#     print(q)

class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node, value:int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def inorder(node: Node) -> None:
    #inorder left, root, right
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Node, value: int) -> bool:
    if node is Node:
        return False
    if node.value == value:
        return True
    elif 





if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 2)
    inorder(root)
    print(search(root, 3))
