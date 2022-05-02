class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def up(pointer, count):
    for _ in range(count):
        pointer = pointer.prev
    return pointer


def down(pointer, count):
    for _ in range(count):
        pointer = pointer.next
    return pointer


def delete(pointer, deleted_rows):
    deleted_rows.append(pointer)
    if pointer.prev is not None:
        pointer.prev.next = pointer.next
    if pointer.next is not None:
        pointer.next.prev = pointer.prev

    if pointer.next is not None:
        pointer = pointer.next
    else:
        pointer = pointer.prev
    return pointer


def undo_delete(deleted_rows):
    latest_row = deleted_rows.pop()
    if latest_row.prev is not None:
        latest_row.prev.next = latest_row
    if latest_row.next is not None:
        latest_row.next.prev = latest_row


def match_table(table, n):
    result = ""
    for i in range(n):
        if table is None:
            result += "X"
        elif table.data == i:
            result += "O"
            table = table.next
        else:
            result += "X"
    return result


def top(pointer):
    while pointer.prev is not None:
        pointer = pointer.prev
    return pointer


def solution(n, k, cmd):
    prev_row = None
    pointer = None
    for i in range(n):
        new_row = Node(i)
        if i == k:
            pointer = new_row
        if prev_row is not None:
            prev_row.next = new_row
            new_row.prev = prev_row
        prev_row = new_row

    deleted_rows = []
    for command in cmd:
        command = command.split()
        if command[0] == "U":
            pointer = up(pointer, int(command[1]))
        elif command[0] == "D":
            pointer = down(pointer, int(command[1]))
        elif command[0] == "C":
            pointer = delete(pointer, deleted_rows)
        elif command[0] == "Z":
            undo_delete(deleted_rows)

    table = top(pointer)

    return match_table(table, n)
