from bracket_control import isBalanced

def test_one_argument():
    assert isBalanced('(') == "NO"
    assert isBalanced('{') == "NO"
    assert isBalanced('[') == "NO"
    assert isBalanced(')') == "NO"
    assert isBalanced('}') == "NO"
    assert isBalanced(']') == "NO"

def test_multiple_non_pair():
    assert isBalanced('())') == "NO"
    assert isBalanced('(()') == "NO"
    assert isBalanced(')()') == "NO"
    assert isBalanced('{}}') == "NO"
    assert isBalanced('{{}') == "NO"
    assert isBalanced('}{}') == "NO"
    assert isBalanced('[]]') == "NO"
    assert isBalanced('[[]') == "NO"
    assert isBalanced('][]') == "NO"

def test_one_correct_placed_pair():
    assert isBalanced('()') == "YES"
    assert isBalanced('{}') == "YES"
    assert isBalanced('[]') == "YES"
    
def test_one_incorrect_placed_pair():
    assert isBalanced('(]') == "NO"
    assert isBalanced('[)') == "NO"
    assert isBalanced('{]') == "NO"
    assert isBalanced(')(') == "NO"
    assert isBalanced('][') == "NO"
    assert isBalanced('}{') == "NO"
    
def test_multiple_correct_placed_pair():
    assert isBalanced('()()()') == "YES"
    assert isBalanced('((()))') == "YES"
    assert isBalanced('()[]{}') == "YES"
    assert isBalanced('[[[]]]') == "YES"
    assert isBalanced('([{()}])') == "YES"
    
def test_multiple_incorrect_placed_pair():
    assert isBalanced('([{]})') == "NO"
    assert isBalanced(')(][}{') == "NO"
    assert isBalanced('][({})') == "NO"