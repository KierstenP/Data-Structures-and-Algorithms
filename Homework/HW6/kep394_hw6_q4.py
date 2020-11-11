from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    shallowCopy = DoublyLinkedList()
    for i in lnk_lst:
        shallowCopy.add_last(i)
    return shallowCopy

def deep_copy_linked_list(lnk_lst):
    deepCopy = DoublyLinkedList()
    for i in lnk_lst:
        if type(i) is DoublyLinkedList:
            nested = deep_copy_linked_list(i)
            deepCopy.add_last(nested)
        else:
            deepCopy.add_last(i)
    return (deepCopy)

def test_code():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)
    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    e1 = lnk_lst1.first_node()
    e1_1 = e1.data.first_node()
    e1_1.data = 10
    e2 = lnk_lst2.first_node()
    e2_1 = e2.data.first_node()
    print(e2_1.data)

