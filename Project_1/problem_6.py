#------------------------------------------------------#
#   problem 6 - Union and Intersection
#------------------------------------------------------#

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        cur_head = self.head
        pointer_string = ""
        while cur_head:
            pointer_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return pointer_string

    def append(self, value):
        """ Add a Node to the end of the linked list """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        """ Calculate the size of the link list """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        """ Transforms the linked list content into a list """
        out = set()
        node = self.head
        while node:
            out.add(node.value)
            node = node.next
        return out

def union(llist_1, llist_2):
    """ Calculate the union of two linked lists """
    # convert linked lists to sets
    set_1 = llist_1.to_set()
    set_2 = llist_2.to_set()
    # preform union on sets
    set_union = set_1 | set_2
    # create a linked list out of the union of sets
    llist_union = LinkedList()
    for item in set_union:
        llist_union.append(item)

    return llist_union

def intersection(llist_1, llist_2):
    """ Calculate the intersection of two linked lists """
    # convert linked lists to sets
    set_1 = llist_1.to_set()
    set_2 = llist_2.to_set()
    # preform intersection on sets
    set_intersection = set_1 & set_2
    # create a linked list out of the intersection of sets
    llist_intersection = LinkedList()
    for item in set_intersection:
        llist_intersection.append(item)

    return llist_intersection


# Standard test cases
#---------------------------------------------------
# Test case 1
#---------------------------------------------------
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
# 4 -> 21 -> 6 ->

#---------------------------------------------------
# Test case 2
#---------------------------------------------------
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4))
#

# Edge test cases
#---------------------------------------------------
# Test case 3
#---------------------------------------------------
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
#
print (intersection(linked_list_5,linked_list_6))
#

#---------------------------------------------------
# Test case 4
#---------------------------------------------------
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [9,7,8,9,1,28,6,66]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
# 1 -> 66 -> 6 -> 7 -> 8 -> 9 -> 28 ->
print (intersection(linked_list_7,linked_list_8))
#
