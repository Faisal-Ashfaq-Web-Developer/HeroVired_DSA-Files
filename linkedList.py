
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insertAtStart(self, value):
        new_node = Node(value)
        new_node.next =self.head
        self.head = new_node

    def insertAfterNode(self,value,pointer):
        new_node = Node(value)
        current = self.head
        while current.value != pointer:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end="->")
            current = current.next

if __name__ == "__main__":
    object = LinkedList()
    object.insertAtStart(20)
    object.insertAfterNode(50,20)
    object.insertAtEnd(100)
    object.display()


