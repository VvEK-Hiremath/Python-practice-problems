class Node:
    """Class representing a single node in a linked list."""
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Pointer to the next node

class LinkedList:
    """Class representing the linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Traverse to the end of the list
        last_node.next = new_node  # Link the last node to the new node

    def delete(self, key):
        """Delete the first occurrence of the node with the specified key."""
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next  # Change head
            current = None  # Free memory
            return
        
        # Search for the key to be deleted, keeping track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # If the key was not present in the list
        if current is None:
            return
        
        # Unlink the node from the linked list
        prev.next = current.next
        current = None  # Free memory

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.display()  # Output: 1 -> 2 -> 3 -> None

    ll.delete(2)
    ll.display()  # Output: 1 -> 3 -> None

    ll.delete(1)
    ll.display()  # Output: 3 -> None