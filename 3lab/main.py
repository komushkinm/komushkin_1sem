

if __name__ == "__main__":
    pass 

log = []


def calc(s, depth=0):
    s = s.replace(' ', '')

    def check_parentheses(expr):
        count = 0
        for ch in expr:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    if s.startswith('(') and s.endswith(')'):
        inner = s[1:-1]
        if check_parentheses(inner):
            count = 0
            for ch in inner:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    break
            if count >= 0:
                return calc(inner, depth)

    brackets = 0
    for i, ch in enumerate(s):
        if ch == '(':
            brackets += 1
        elif ch == ')':
            brackets -= 1
        elif brackets == 0 and ch in '+-':
            a = calc(s[:i], depth + 1)
            b = calc(s[i + 1:], depth + 1)
            res = a + b if ch == '+' else a - b
            log.append(f"{'  ' * depth}{ch}: {s} = {res}")
            return res

    brackets = 0
    for i, ch in enumerate(s):
        if ch == '(':
            brackets += 1
        elif ch == ')':
            brackets -= 1
        elif brackets == 0 and ch in '*/':
            a = calc(s[:i], depth + 1)
            b = calc(s[i + 1:], depth + 1)
            res = a * b if ch == '*' else a / b
            log.append(f"{'  ' * depth}{ch}: {s} = {res}")
            return res

    log.append(f"{'  ' * depth}число: {int(s)}")
    return float(s)


expr = str(input())
log = []
try:
    result = calc(expr)
    for l in log:
        print(l)
    print(f"\nРезультат: {result}")
except:
    print("ошибка в примере")
