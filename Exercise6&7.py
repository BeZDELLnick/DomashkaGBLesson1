def int_func(n):
    return n[:1].upper() + n[1:]


print(int_func(input("Введите слово: ")))

n = input("Вверите строку с пробелами: ")
str_funk = n.split()
new = []
for i in range(len(str_funk)):
    new.append(int_func(str_funk[i]))
print(*new)
