# Define a ListNode class that represents elements of a linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create a class named Solution to encapsulate the solution functions.
class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next


# Example linked lists (you can customize these).
# Instead of using lists, create ListNode objects directly.
list1 = ListNode(9)
list1.next = ListNode(9)
list1.next.next = ListNode(9)
# ...
list2 = ListNode(9)
list2.next = ListNode(9)
list2.next.next = ListNode(9)
# ...

solution = Solution()
result = solution.addTwoNumbers(list1, list2)
# After you obtain the result from the addTwoNumbers method, you can use this loop to print the values.
current = result  # Start from the first node (head) of the result-linked list
while current:
    print(current.val, end=" ")
    current = current.next  # Move to the next node
print()


# This will print each value in the linked list.

# Example:
# If the linked list contains 2 -> 4 -> 3, the loop will print:
# 2
# 4
# 3

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name} ({self.email})"


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)  # Call the __str__ method of the contained object


# Create customer objects
customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")

# Create node objects with customer data
node1 = Node(customer1)
node2 = Node(customer2)

# Link the nodes in a linked list
node1.next_node = node2

# Printing the linked list will call the __str__ method of Node and, in turn, the __str__ method of the contained
# Customer object
current_node = node1

while current_node:
    print(current_node)
    current_node = current_node.next_node


class MyObject:
    def __init__(self, val=0):
        self.val = val


# Creating instances of MyObject with different initial values
obj1 = MyObject()  # Defaults to val=0
obj2 = MyObject(42)  # Initializes val to 42
obj3 = MyObject(None)  # Could lead to unexpected behavior and type issues


# Define a class for individual nodes in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute of the node
        self.next = None  # Initialize the next attribute (forward reference) to None
        self.prev = None  # Initialize the prev attribute (backward reference) to None


# Define a class for a doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    # Method to append a new node with the given data to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        if self.head is None:  # If the list is empty (head is None)
            self.head = new_node  # Set the head to the new node
        else:
            current = self.head  # Start from the head node
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Set the next reference of the last node to the new node
            new_node.prev = current  # Set the previous reference of the new node to the last node

    # Method to traverse the list in the forward direction and print its elements
    def traverse_forward(self):
        current = self.head  # Start from the head node
        while current:  # While there are nodes to traverse
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the list

    # Method to traverse the list in the backward direction and print its elements
    def traverse_backward(self):
        current = self.head  # Start from the head node
        while current and current.next:  # Traverse to the end of the list
            current = current.next
        while current:  # Traverse backward from the last node
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.prev  # Move to the previous node
        print("None")  # Print "None" to indicate the end of the list


# Create an instance of the DoublyLinkedList class
dll = DoublyLinkedList()

# Append nodes with data to the doubly linked list
dll.append(1)
dll.append(2)
dll.append(3)

# Traversing the list forward and backward and printing its elements
dll.traverse_forward()  # Output: 1 -> 2 -> 3 -> None
dll.traverse_backward()  # Output: 3 -> 2 -> 1 -> None

