"""
Queue to stack converter.
"""
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue


def queue_to_stack(queue):
    """
    Method converts queue to stack.
    """
    queue_copy = LinkedQueue(queue)
    stack = LinkedStack()
    elements = []
    while not queue_copy.isEmpty():
        element = queue_copy.pop()
        elements.append(element)
    elements = elements[::-1]

    for _ in range(len(elements)):
        stack.push(elements[_])
    return stack
