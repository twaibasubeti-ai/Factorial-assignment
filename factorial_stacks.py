# ============================================================
# DATA STRUCTURES AND ALGORITHMS - TASK TWO
# Factorial Using Forward and Backward Stacks
# ============================================================


# ============================================================
# MODULE 1: STACK DATA STRUCTURE
# ============================================================

class Stack:
    """
    A Stack is a LIFO (Last In, First Out) data structure.

    The last element added to the stack is the first element
    removed from the stack.
    """

    def __init__(self):
        # List is used to store the stack elements
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")

        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")

        return self.items[-1]

    def is_empty(self):
        """
        Check whether the stack is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the stack.
        """
        return len(self.items)

    def display(self):
        """
        Display the contents of the stack.
        """
        return self.items


# ============================================================
# MODULE 2: FORWARD STACK FACTORIAL
# ============================================================

def factorial_forward(n):
    """
    Calculate n! using a forward stack.

    Values are pushed in descending order:

        n, n-1, n-2, ..., 1

    Because a stack follows LIFO, they are popped in
    ascending order:

        1, 2, 3, ..., n

    Therefore the multiplication happens as:

        1 × 2 × 3 × ... × n
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    stack = Stack()

    # PUSH PHASE
    # Push numbers from n down to 1
    for number in range(n, 0, -1):
        stack.push(number)

    print("\nFORWARD STACK")
    print("----------------------------")
    print("Push order:", stack.display())

    # POP PHASE
    result = 1

    print("Pop and multiplication order:")

    while not stack.is_empty():
        number = stack.pop()
        result = result * number

        print(
            f"Pop {number} -> "
            f"Current result = {result}"
        )

    return result


# ============================================================
# MODULE 3: BACKWARD STACK FACTORIAL
# ============================================================

def factorial_backward(n):
    """
    Calculate n! using a backward stack.

    Values are pushed in ascending order:

        1, 2, 3, ..., n

    Because a stack follows LIFO, they are popped in
    descending order:

        n, n-1, n-2, ..., 1

    Therefore the multiplication happens as:

        n × (n-1) × ... × 2 × 1
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    stack = Stack()

    # PUSH PHASE
    # Push numbers from 1 up to n
    for number in range(1, n + 1):
        stack.push(number)

    print("\nBACKWARD STACK")
    print("----------------------------")
    print("Push order:", stack.display())

    # POP PHASE
    result = 1

    print("Pop and multiplication order:")

    while not stack.is_empty():
        number = stack.pop()
        result = result * number

        print(
            f"Pop {number} -> "
            f"Current result = {result}"
        )

    return result


# ============================================================
# MODULE 4: DISPLAY FACTORIAL SEQUENCE
# ============================================================

def display_factorial_sequence(n):
    """
    Display the normal factorial sequence.

    Example for n = 5:

    1! = 1
    2! = 1 × 2 = 2
    3! = 2 × 3 = 6
    4! = 6 × 4 = 24
    5! = 24 × 5 = 120
    """

    print("\nFACTORIAL SEQUENCE")
    print("----------------------------")

    result = 1

    for number in range(1, n + 1):
        result = result * number

        if number == 1:
            print(f"{number}! = {result}")
        else:
            print(
                f"{number}! = "
                f"{result // number} x {number} = {result}"
            )


# ============================================================
# MODULE 5: MAIN PROGRAM
# ============================================================

def main():

    print("=" * 55)
    print("       FACTORIAL USING STACKS")
    print("       DATA STRUCTURES AND ALGORITHMS")
    print("=" * 55)

    # Get input from the user
    while True:

        try:
            n = int(input("\nEnter a non-negative integer n: "))

            if n < 0:
                print("Please enter a non-negative number.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Display the factorial sequence
    display_factorial_sequence(n)

    # Calculate using forward stack
    forward_result = factorial_forward(n)

    # Calculate using backward stack
    backward_result = factorial_backward(n)

    # ========================================================
    # VERIFICATION
    # ========================================================

    print("\n")
    print("=" * 55)
    print("RESULTS")
    print("=" * 55)

    print(f"n = {n}")
    print(f"Forward Stack Result  = {forward_result}")
    print(f"Backward Stack Result = {backward_result}")

    if forward_result == backward_result:
        print("\nBoth stack implementations produced the same result.")
        print(f"{n}! = {forward_result}")
    else:
        print("\nERROR: The two implementations produced different results.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()