from stack import Stack


def check_brackets(expression: str) -> bool:
    close_bracket = [')', ']', '}']
    match = {
        '(': ')',
        '[': ']',
        '{': '}',
        '"': '"',
        "'": "'"
    }
    balance = Stack()
    for letter in expression:
        if balance.peek() == letter:
            balance.pop()
            continue
        if letter in close_bracket:
            return False
        if letter in match:
            balance.push(match[letter])
    return balance.isempty()


if __name__ == "__main__":
    while True:
        exp = input("Введите выражение: ")
        if not exp:
            exit()
        if check_brackets(exp):
            print("Сбалансированно")
        else:
            print("Несбалансированно")
        print()
