def solution(p):
    def check_bracket(p):
        count = 0
        success = True
        first_balanced_index = -1
        for i, c in enumerate(p):
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            else:
                continue

            if count < 0:
                success = False
            elif first_balanced_index == -1 and count == 0:
                first_balanced_index = i + 1

        if count == 0:
            if success:
                return 0  # 올바른 괄호
            return first_balanced_index  # 균형잡힌 괄호
        return -1

    def reverse(p):
        new_p = ''
        for i, c in enumerate(p):
            if c == '(':
                new_p += ')'
            elif c == ')':
                new_p += '('
            else:
                new_p += p[i]

        return new_p

    def convert(p):
        split_index = check_bracket(p)
        if split_index == 0:
            return p
        u = p[:split_index]
        v = p[split_index:]

        if check_bracket(u) == 0:
            return u + convert(v)

        return '(' + convert(v) + ')' + reverse(u[1:-1])

    return convert(p)
