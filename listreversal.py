lst = list(map(int, input("Enter list elements separated by space: ").split()))
start, end = 0, len(lst) - 1
while start < end:
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1
print("Reversed List:", lst)
