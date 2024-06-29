from dataclasses import dataclass, field
from typing import List, Optional


DEFAULT_LINKED_LIST = 'a,b,c,d,e,f'


@dataclass
class Node:
    value: str = ''
    previous: 'Node' = None
    next: 'Node' = None


@dataclass
class LinkedList:
    nodes: Optional[List] =  field(default_factory=list)

    def create_nodes(
        self,
        nodes: str,
        ):
        values = sorted(nodes.split(","))
        prev_node = None

        for value in values:
            new_node = Node(value=value, previous=prev_node)
            if prev_node:
                prev_node.next = new_node
            self.nodes.append(new_node)
            prev_node = new_node

    def print_list(self):
        current = self.nodes[0] if self.nodes else None
        while current:
            print(current.value, end=" - " if current.next else "\n")
            current = current.next

    def find_node(self, value: str) -> Optional[Node]:
        current = self.nodes[0] if self.nodes else None
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete_node(self, value: str):
        node = self.find_node(value)
        if not node:
            raise ValueError("El nodo no ha sido encontrado")
        if not node.next:
            node.previous.next = None
        else:
            node.value = node.next.value
            node.next = node.next.next
            if node.next:
                node.next.previous = node
