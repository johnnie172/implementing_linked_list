class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Linked_List:

    def __init__(self):
        self.head = None

    def __str__(self):
        next_node = self.head
        linked_list_str = ''
        while next_node is not None:
            linked_list_str += str(next_node.value) + " "
            next_node = next_node.next_node

        return linked_list_str

    def insert(self, value):
        if self.head is None:
            first_node = Node(value, self.head)
            self.head = first_node
        else:
            current_node = self.head
            new_node = Node(value)

            while current_node.next_node is not None:
                current_node = current_node.next_node

            current_node.next_node = new_node

    def insert_by_index(self, value, index):
        current_node = self.head
        new_node = Node(value)

        if self.head is None and index != 0:
            raise Exception('The list is empty, can only insert to index 0')

        if self.head is None and index == 0:
            self.head = new_node

        if self.head is not None and index == 0:
            new_node.next_node = current_node
            self.head = new_node
        else:
            try:
                for i in range(index - 1):
                    current_node = current_node.next_node

                new_node.next_node = current_node.next_node
                current_node.next_node = new_node

            except AttributeError:
                raise Exception('Your list do not contained that index number')

    def replace_by_index(self, value, index):

        current_index = 0
        current_node = self.head
        new_node = Node(value)
        if self.head is None and index != 0:
            raise Exception('The list is empty, can only insert to index 0')
        else:
            try:

                while current_index != index:
                    current_node = current_node.next_node
                    current_index += 1

                new_node.next_node = current_node.next_node
                current_node.next_node = new_node.next_node
                current_node.value = new_node.value
            except AttributeError:
                raise Exception('Your list do not contained that index number')

        # insert value to the list at the given index

    def remove_by_index(self, index):
        current_node = self.head
        new_index = index - 1
        i_count = 0
        if self.head is None:
            raise Exception("The list is empty, can't remove any index.")

        if self.head is not None and index == 0:
            self.head = current_node.next_node

        if self.head is not None and index == 1:
            new_next_node = current_node
            current_node = current_node.next_node
            new_next_node.next_node = current_node.next_node

        else:
            try:
                for i in range(index - 1):
                    current_node = current_node.next_node
                    new_next_node = current_node
                    i_count += 1
                    if i_count == new_index:
                        current_node = current_node.next_node
                        new_next_node.next_node = current_node.next_node
                        # new_next_node.value = current_node.value

            except AttributeError:
                raise Exception('Your list do not contained that index number')

    def find(self, value):
        # find the element with the given value. return it's index in the list
        current_node = self.head
        current_node_value = None
        index = 0

        if current_node is None:
            raise Exception('The list is empty')

        if current_node.value == value:
            return index

        else:
            try:
                while current_node_value != value:
                    current_node = current_node.next_node
                    current_node_value = current_node.value
                    index += 1
            except AttributeError:
                pass

        if current_node_value == value:
            return index
        else:
            print('The value have not found.')
            return None

    def get(self, index):
        # find the element in the given index and return its value
        current_node = self.head
        index_count = 0

        if current_node is None:
            raise Exception('The list is empty')

        current_node_value = current_node.value

        if index == 0:
            return current_node_value
        else:
            try:
                for i in range(index):
                    index_count += 1
                    current_node = current_node.next_node
                    current_node_value = current_node.value
                    if current_node.value is not None and index_count == index:
                        return current_node_value
            except AttributeError:
                raise Exception('Your list does not have that index.')

    def count(self):
        current_node = self.head

        if current_node is None:
            return 0
        else:
            next_node = current_node.next_node
            node_counter = 0
            try:
                if next_node is None:
                    return 1
                while next_node is not None:
                    current_node = current_node.next_node
                    node_counter += 1
                    continue
            except AttributeError:
                return node_counter

