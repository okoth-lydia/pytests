# a simple pytest function
def test_one_plus_one():
    assert 1 + 1 == 2

# a failing testcase
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c # assertion introspection

# handling exceptions to avoid false negatives

def test_divide_by_zero():
    num = 1/0

