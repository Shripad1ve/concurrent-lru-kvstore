import threading
from typing import Optional, Any

class Node:
    def __init__(self, key: str, val: Any):
        self.key: str = key
        self.val: Any = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class ThreadSafeLRUCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.cache: dict[str, Node] = {}
        self.lock = threading.Lock()

        # Dummy head and tail to eliminate null boundary checks
        self.head = Node("__HEAD__", None)
        self.tail = Node("__TAIL__", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Splice node out of current position."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_head(self, node: Node) -> None:
        """Insert node immediately after dummy head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key not in self.cache:
                return None
            node = self.cache[key]
            self._remove(node)
            self._insert_at_head(node)
            return node.val

    def put(self, key: str, value: Any) -> None:
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                node.val = value
                self._remove(node)
                self._insert_at_head(node)
                return

            if len(self.cache) >= self.capacity:
                # Evict the node right before dummy tail (least recently used)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_at_head(new_node)
