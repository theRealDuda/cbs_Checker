def is_cbs(seq):
    stack = []
    for i in seq:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        return True
    return False
                
def need_to_move(seq):
    stack = []
    for i in seq:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    a = stack.count('(')
    b = stack.count(')')
    return max(a,b)

print(need_to_move("(()))("))