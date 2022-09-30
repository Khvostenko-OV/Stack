import pytest
from stack import Stack
from main import check_brackets


def test_stack():
    st = Stack()
    assert st.isempty()
    st.push("1")
    st.push(2)
    assert st.peek() == 2
    assert st.pop() == 2
    assert st.size() == 1
    assert not st.isempty()
    assert st.pop() == "1"
    assert st.isempty()
    assert st.peek() == None
    assert st.pop() == None

fixture1 = [
    ("(((([{}]))))", True),
    ("[([])((([[[]]])))]{()}", True),
    ("{{[()]}}", True),
    ("}{}", False),
    ("{{[(])]}}", False),
    ("[[{())}]", False),
    ("((())", False)
    ]

@pytest.mark.parametrize("exp, result", fixture1)
def test_check_brackets(exp, result):
    assert check_brackets(exp) == result
