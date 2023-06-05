from Stacks.StackBasedList import StackListBased


def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        stack = StackListBased()
        for i in range(2, num + 1):
            stack.push(i)
        while len(stack) > 1:
            stack.push(stack.pop() * stack.pop())
        return stack.peek()

print(fatorial(7))
