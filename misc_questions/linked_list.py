

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class LinkedList:

    def __init__(self, head_node):
        self.head_node = head_node

    def add_node(self, node):

        index_node = self.head_node
        while index_node.next != None:
            index_node = index_node.next

        index_node.next = node
        node.prev = index_node


    def print_vals(self):


        index_node = self.head_node
        while index_node != None:
            print(index_node.val)
            index_node = index_node.next

    def insert_after(self, val, node):

        index_node = self.head_node
        while index_node != None:
            index_node = index_node.next

            if index_node.val == val:
                next_node = index_node.next
                index_node.next = node
                node.prev = index_node
                node.next = next_node
                break



if __name__ == "__main__":


    head_node = Node(1)

    linked_list = LinkedList(head_node)
    linked_list.add_node(Node(2))
    linked_list.add_node(Node(3))
    linked_list.add_node(Node(4))

    linked_list.print_vals()

    linked_list.insert_after(2, Node(2.5))

    linked_list.print_vals()


