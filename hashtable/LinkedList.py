### Linked List ###
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 1

    def add_to_head(self, value):
        if self.head is None:
            node = Node(value)
        else:
            prev = self.head
            self.head = Node(value, prev)

        self.size =+ 1

    def remove_from_head(self):
        if self.head is None:
            return

        current_head = self.head
        new_head = current_head.next
        current_head = None
        self.head = new_head

        self.size =- 1

    def remove(self, value):
        current = self.head
        # if there is nothing to delete
        if current is None:
            return None
        # when deleting head
        if current.value[0] == value:
            self.head = current.next
            return current
        # when deleting something else
        else:
            previous = current
            current = current.next
            while current is not None:
                if current.value[0] == value: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node
                else:
                    previous = current
                    current = current.next
            return None # if we got here, nothing was found!

    def __len__(self):
        return self.size

    def __str__(self):
        current_node = self.head
        total = 0
        str = ""
        while current_node != None:
            str += f"index {total}: key => {current_node.value[0]}, value => {current_node.value[1]}\n"
            # str += f"index {total}: length {len(self)} \n"
            current_node = current_node.next
            total += 1
        return str
