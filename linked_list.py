"""
DoubleLinkedList(더미 연결 리스트)
- Object
    - 순서 있는 언소의 유한 집합
- Operation
1. empty() -> Boolean
비어 있으면 True, 아니면 False
2. size() -> Integer
요소 개수 변환
3. add_first(data)
data를 리스트의 맨 앞에 추가
4. add_last(data)
data를 리스트의 맨 마지막에 추가
5. insert_after(data, node)
data를 node 다음에 삽입
6. insert_before(data, node)
data를 node 이전에 삽입
7. search_forward(target) -> node
target을 리스트의 맨 처음부터 찾아 나가다 리스트에 있으면 노드 반환, 그렇지 않으면 None 반환
8. search_backward(target) -> node
target을 리스트의 맨 마지막부터 찾아 나가다 리스트에 있으면 노드 반환, 그렇지 않으면 None 반환
9. delete_first()
리스트의 첫 번쨰 요소 삭제
10. delete_last()
리스트의 마지막 요소 삭제
11. delete_node(node)
node 삭제
"""
from typing import Union


class Node(object):
    """
    연결 리스트에 들어갈 노드
    """

    def __init__(self, data=None):
        self._data = data
        self._prev = None
        self._next = None

    # 소멸자: 객체가 사라지기 전 반드시 호출된다.
    # 삭제 연산 때 삭제되는 것을 확인하고자 작성
    def __del__(self):
        pprint(f"data of {self._data} is deleted")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, p):
        self._prev = p

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않는 노드이다.
        # 이를 더미 노드라고 한다.
        self.head = Node()
        self.tail = Node()
        # 초기화
        self.head.next = self.tail
        self.tail.prev = self.head
        # 데이터 개수를 저장할 변수이다.
        self.d_size = 0

    def empty(self) -> bool:
        return self.d_size == 0  # 비어있는 지 확인

    def size(self) -> int:
        return self.d_size

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        new_node = Node(data)

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    def insert_after(self, data, node: Node):
        new_node = Node(data)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node = Node(data)

        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node

        self.d_size += 1

    def search_forward(self, target) -> Union[Node, None]:
        cur = self.head.next

        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target) -> Union[Node, None]:
        cur = self.tail.prev
        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None

    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1


def show_list(dlist: DoubleLinkedList):
    pprint('data size : {}'.format(dlist.size()))
    cur = dlist.head.next
    while cur is not dlist.tail:
        pprint(cur.data)
        cur = cur.next


if __name__ == "__main__":
    from pprint import pprint

    dlist = DoubleLinkedList()
    pprint('*' * 100)
    pprint('데이터 삽입 -add_first')
    dlist.add_first(1)
    dlist.add_first(2)

    pprint('데이터 삽입 -add_last')
    dlist.add_last(3)
    dlist.add_last(4)
    dlist.add_last(5)
    show_list(dlist)

    pprint('데이터 삽입 - insert_after')
    dlist.insert_after(4, dlist.search_forward(3))
    show_list(dlist)

    pprint('데이터 삽입 - insert_before')
    dlist.insert_before(4, dlist.search_forward(5))
    show_list(dlist)

    pprint('데이터 탐색')
    target = 3
    # res=dlist.search_forward(target)
    res = dlist.search_backward(target)
    if res:
        pprint('데이터 {} 탐색 성공'.format(res.data))
    else:
        pprint('데이터 {} 탐색 실패'.format(target))
    res = None

    # pprint('데이터 삭제-delete_first')
    # dlist.delete_first()
    # dlist.delete_first()

    # pprint('데이터 삭제-delete_last')
    # dlist.delete_last()
    # dlist.delete_last()

    pprint('데이터 삭제-delete_node')
    dlist.delete_node(dlist.search_backward(5))

    show_list(dlist)

    pprint('*' * 100)
