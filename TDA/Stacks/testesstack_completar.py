from Stacks.StackBasedList import StackListBased

def test(stack):
    print("Length ", len(stack))
    print("Empty? ", stack.is_empty())
    print("Push 1-10")
    for i in range(1, 11):
        stack.push(i)
    print("Items bottom to top: ", stack)
    print("Peeking ", stack.peek())
    print("Length ", len(stack))
    print("Empty? ", stack.is_empty())
    the_clone = StackListBased()
    for item in stack:
        the_clone.push(item)
    print("Clone ", the_clone)
    the_clone.clear()
    print("Length of clone after clear", len(the_clone))
    print("Clone is Empty? ", the_clone.is_empty() )
    print("Push 11", stack.push(11))
    print("Items bottom to top: ", stack)
    print("Popping items top to bottom: ")
    while not stack.is_empty():
        print("popping ...", stack.pop())
    print("Empty? ", stack.is_empty() )

test(StackListBased())
