# stack using list

stack = []

# push (add element)
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

# pop (remove top element)
stack.pop()
print("Stack after pop:", stack)

# peek (top element)
print("Top element:", stack[-1])

# check if empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
