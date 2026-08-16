# Day 3: im gonna learn ab Recursion, Stack and Queue

# Recursion: the self-calling function (đệ quy)
# is a programming technique where a function calls itself to solve the smaller instances of the same problem
# every recursive func must have a "base case" to stop the self-calling loop
def calculate_factorial(n):
    # base case: if n = 0 or n = 1, end loop
    if n == 0 or n == 1:
        return 1

    # recursive case: n * recall(n-1)
    else:
        return n * calculate_factorial(n-1)

print("factorial of 5 is:", calculate_factorial(5))
# output: 120 (5 * 4 * 3 * 2 * 1 = 120), end loop at n=1

# -------------------------------------------------------------------------------------

# Stack: LIFO principle
# is a linear data structure that follows the Last in, First out principle
# this means i can only take the last added item out first
# in Python, we can simply use a List to simulate a Stack
# using append() to push item in the top of Stack, pop() to remove the top item
ml_model_stack = []

# push items in using append()
ml_model_stack.append("model_1")
ml_model_stack.append("model_2")
ml_model_stack.append("model_3")
print("stack append method:", ml_model_stack)

# remove the top one using pop()
ml_model_stack.pop()
print("stack pop method:", ml_model_stack)

# -------------------------------------------------------------------------------------

# Queue: FIFO principle
# is a linear data structure that follows the First in, First out principle
# this means the item added first will be removed first, like a line of people (whoever queue first will be served first)
# but unlike stack, using list as a queue is slower than using a deque (collections). Why?
# using pop(0) in a List-based Queue, Python has to shift all the other items to the left to fill the space of the removed item
# but popleft() in a deque (doubly-linked list), Python just has to delete the pointer pointing to the first item then point to the next one
from collections import deque
label_queue = deque()

label_queue.append("dog")
label_queue.append("cat")
label_queue.append("fish")

print("queue append method:", list(label_queue))

label_queue.popleft()
print("queue pop method:", list(label_queue))