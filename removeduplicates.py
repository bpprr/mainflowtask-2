lst = list(map(int, input("Enter list elements separated by space: ").split()))
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print("List after removing duplicates:", unique)
