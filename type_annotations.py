from typing import TypeVar, Generic, Iterable
from collections import defaultdict, UserDict


def reverse(coll: list) -> list:
    return coll[::-1]


# Enforce return type to be the same as the input type
T = TypeVar('T')


def reverse_t(coll: list[T]) -> list[T]:
    return coll[::-1]


Node = TypeVar("Node")
Edge = TypeVar("Edge")


# directed graph
class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node,  list[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relations(self, node: Node) -> list[Edge]:
        return self.edges[node]


def get_aliases(item) -> Iterable:
    pass


class NutritionalInformation(UserDict):
    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError:
            pass
        for alias in get_aliases(item):
            try:
                return self.data[alias]
            except KeyError:
                pass
        raise KeyError(f"Could not find {item} or any of its aliases")
