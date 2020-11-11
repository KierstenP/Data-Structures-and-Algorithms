
class Empty(Exception):
    pass

class EmptyTree(Exception):
    pass
    
class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum


    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return 0
        elif (subtree_root.left is not None):
            return 1 + self.subtree_height(subtree_root.left)
        elif (subtree_root.right is not None):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.postorder():
            yield node.data

def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree
    if bin_tree.root.left is None and bin_tree.root.right is None:
        tup = bin_tree.root.data, bin_tree.root.data
        return tup
    def subtree_min_and_max(bin_tree, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return subtree_root.data
        else:
            if subtree_root.left is not None:
                left_sum = subtree_min_and_max(bin_tree, subtree_root.left)
                check = subtree_root.data
                if type(left_sum) is int:
                    if check < left_sum:
                        left_sum = (check, left_sum)
                    else:
                        left_sum = (left_sum, check)
                else:
                    if check < left_sum[0]:
                        left_sum = (check, left_sum[1])
                    if check > left_sum[1]:
                        left_sum = (left_sum[0], check)
            else:
                left_sum = subtree_root.data
            if subtree_root.right is not None:
                right_sum = subtree_min_and_max(bin_tree, subtree_root.right)
                check = subtree_root.data

                if type(right_sum) is int:
                    if check < right_sum:
                        right_sum = (check, right_sum)
                    else:
                        right_sum = (right_sum, check)
                else:
                    if check < right_sum[0]:
                        right_sum = (check, right_sum[1])
                    if check > right_sum[1]:
                        right_sum = (right_sum[0], check)
            else:
                right_sum = subtree_root.data
            if isinstance(right_sum, int) and isinstance(left_sum, int):  # If both of the comparisons are integer...
                if left_sum > right_sum:  # If the left side of the branch is bigger, than, return...
                    tuple = (right_sum, left_sum)  # Min, Max
                    return tuple
                if right_sum > left_sum:  # If left side is smaller, return...
                    tuple = (left_sum, right_sum)  # Min, max
                    return tuple
            elif type(left_sum) is not int and type(
                    right_sum) is int:  # If the left side is a tuple.. but right side isn't...
                # Compare the right versus both the min of the tuple and max of the tuple
                minTuple = left_sum[0]
                maxTuple = left_sum[1]

                newTuple = (minTuple, maxTuple)
                if right_sum < minTuple:
                    newTuple = (right_sum, maxTuple)
                if right_sum > maxTuple:
                    newTuple = (minTuple, right_sum)
                return newTuple
            if type(left_sum) is int and type(
                    right_sum) is not int:  # If the right side is a tuple.. but left side isn't...
                # Compare the left_sum versus both the min of the tuple and max of the tuple
                minTuple = right_sum[0]
                maxTuple = right_sum[1]

                newTuple = (minTuple, maxTuple)
                if left_sum < minTuple:
                    newTuple = (left_sum, maxTuple)
                if left_sum > maxTuple:
                    newTuple = (minTuple, left_sum)
                return newTuple
            else:
                # If both are tuples... compare each min and max...
                leftMin = left_sum[0]
                rightMin = right_sum[0]

                leftMax = left_sum[1]
                rightMax = right_sum[1]

                newMin = 0
                newMax = 0

                if leftMin < rightMin:
                    newMin = leftMin
                else:
                    newMin = rightMin
                if leftMax > rightMax:
                    newMax = leftMax
                else:
                    newMax = rightMax
                newTuple = (newMin, newMax)
                return newTuple
    root = bin_tree.root
    #HELPER FUNCTION
    return subtree_min_and_max(bin_tree, root)


