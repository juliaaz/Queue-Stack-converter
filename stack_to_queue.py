"""
Stack to queue converter.
"""
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

def stack_to_queue(stack):
    """
    Method converts stack to queue.
    """
    stack_copy = LinkedStack(stack)
    queue = LinkedQueue()
    while not stack_copy.isEmpty():
        element = stack_copy.pop()
        queue.add(element)

    return queue
