#------------------------------------------------------#
#   problem 1 - Least Recently Used Cache
#------------------------------------------------------#

class DoubleNode:
    def __init__(self, key, value):
        """ Node for a doubly linked list """
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DNode(key: {}, value: {})".format(self.key, self.value)


class LRU_Cache:
    def __init__(self, cache_size):
        """ implementation of the LRU cache """

        # if cache size is not valid
        if cache_size is None or cache_size < 1:
            print("Value error: Minimum cache size is 1")
            return
        self.cache_size = cache_size
        self.current_size = 0

        # dubbly liked list
        self.head = None
        self.tail = None

        # hash map (dictionary) for fast look up
        self.cache_map = dict()


    def get(self, key):
        """ return value for the input key """

        ## hash map
        # get DoubleNode from hash map
        node = self.cache_map.get(key)

        if node is None:
            return -1

        ## doubly linked list (dll)
        # special case node is already head node
        if node == self.head:
            return node.value

        # remove node from dll and add as head
        self.remove(node)
        self.prepend(node)

        return node.value


    def set(self, key, value):
        """ set value with key """

        # if key is already in the cache map
        if key in self.cache_map:
            node = self.cache_map[key]
            value = node.value
            ## dll
            if node != self.head:
                self.remove(node)
                self.prepend(node)
        else:
            node = DoubleNode(key, value)
            if self.cache_size == self.current_size:
                del self.cache_map[self.tail.key]
                self.remove(self.tail)
            else:
                self.current_size += 1
            self.cache_map[key] = node
            self.prepend(node)


    def prepend(self, node):
        """ DLL Prepend a value to the beginning of the list. """

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.head
            self.head.next = node
            self.head = node


    def remove(self, node):
        """ DLL Remove node form list """
        # no node in LRUCache
        if self.head is None:
            return
        # node in the middle
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        # node at the tail
        if self.tail == node:
            self.tail = node.next
        # node at the head
        if (node.next is None) and (node.previous is None):
            self.head = None
            self.tail = None


    def print_linked_list(self):
        node = self.head
        while node:
            print("{} -> ".format(node))
            node = node.previous
        print("NULL")


    def print_map(self):
        print(self.cache_map)


# Standard test cases
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(9))
# -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# -1 because the cache reached it's size and 3 was the least recently used entry

# Edge test cases
our_cache = LRU_Cache(0)
# Value error: Minimum cache size is 1
our_cache = LRU_Cache(None)
# Value error: Minimum cache size is 1
our_cache = LRU_Cache(2)
print(our_cache.get(2))
# -1
