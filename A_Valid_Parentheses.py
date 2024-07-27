stack = []
    valid = [False] * len(s)
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                opening_index = stack.pop()
                valid[opening_index] = True
                valid[i] = True
    
    max_length = 0
    current_length = 0
    
    for v in valid:
        if v:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    
    return max_length