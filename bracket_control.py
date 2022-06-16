def isBalanced(s):
    brackets = []
    open_bracket = ['(', '[', '{']
    
    for c in s:
        if c in open_bracket:
            brackets.append(c)
        try:
            if c == ')':
                if brackets.pop() != '(':
                    return "NO"
            elif c == '}':
                if brackets.pop() != '{':
                    return "NO"
            elif c == ']':
                if brackets.pop() != '[':
                    return "NO"
        except:
            return "NO"
            
    if len(brackets) == 0:
        return "YES"
    else:
        return "NO"
