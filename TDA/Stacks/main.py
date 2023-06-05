from Stacks.StackBasedList import StackListBased

'''stack = StackListBased()
print(stack)
stack.push(20)
stack.push(10)
print(stack)
print(stack.peek())
stack.pop()
print(stack.is_empty())
stack.pop()
print(stack.is_empty())'''


def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        stack = StackListBased()
        for i in range(2, num + 1):
            stack.push(i)
        while len(stack) > 1:
            # op1 = stack.pop()
            # op2 = stack.pop()
            # stack.push(op1 * op2)
            stack.push(stack.pop() * stack.pop())
        return stack.peek()

print(fatorial(500))

