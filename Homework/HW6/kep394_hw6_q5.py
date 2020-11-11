from DoublyLinkedList import *

def merge_sublists(link_lst1, link_lst2, returnList):
    if link_lst1.is_empty() and link_lst2.is_empty():
        return returnList
    if link_lst1.is_empty():
        returnList.add_last(link_lst2.delete_node(link_lst2.first_node()))
        return(merge_sublists(link_lst1, link_lst2, returnList))
    if link_lst2.is_empty():
        returnList.add_last(link_lst1.delete_node(link_lst1.first_node()))
        return(merge_sublists(link_lst1, link_lst2, returnList))
    else:
        temp1 = link_lst1.first_node().data
        temp2 = link_lst2.first_node().data
        if temp1 > temp2:
            returnList.add_last(link_lst2.delete_node(link_lst2.first_node()))
            return merge_sublists(link_lst1, link_lst2, returnList)
        else:
            returnList.add_last(link_lst1.delete_node(link_lst1.first_node()))
            return merge_sublists(link_lst1, link_lst2, returnList)


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    returnList = DoublyLinkedList()
    return(merge_sublists(srt_lnk_lst1, srt_lnk_lst2, returnList))


def test_code():
    link_lst1 = DoublyLinkedList()
    link_lst2 = DoublyLinkedList()
    link_lst1.add_last(1)
    link_lst1.add_last(3)
    link_lst1.add_last(5)
    link_lst2.add_last(2)
    link_lst2.add_last(4)
    link_lst2.add_last(6)
    print(link_lst1)
    print(link_lst2)
    lst3 = merge_linked_lists(link_lst1, link_lst2)
    print(lst3)