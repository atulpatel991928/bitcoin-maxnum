s = []
top = None
def isEmpty(stack):
    if (stack==[]):
        return true
    else:
        return false

def push(stack, item):
    stack.append(item)
    top= len(stack) -1

def pop(stack):
    if (isEmpty(stack)):
        return ('underflow')
    else:
        i = stack.pop()
        if (len(stack)==0):
            top=None
        else:
            top = top-1
    return i


