# 1
hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")
print("Количество повторений:", hashes.count("ffd222"))

# 2
users = ("guest", "moderator", "admin", "root")
print(users.index("admin"))

# 3
key_params = ("AES", 256, "CBC")
algorithm, key_size, mode = key_params
print("Алгоритм:", algorithm)
print("Размер ключа:", key_size)
print("Режим:", mode)

# 4
log = ("login", "download", "upload", "logout")
print("Последний элемент:", log[-1])

# 5
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
ip_input = input("Введите IP-адрес: ")
if ip_input in ips:
    print("Адрес найден")
else:
    print("Нет в списке")

# 6
name = input("Введите имя: ")
role = input("Введите роль: ")
status = input("Введите статус: ")
user_info = (name, role, status)
print("Информация о пользователе:", user_info)

# 7
access = ("read", "write", "execute")
new_word = input("Введите новое слово: ")
print((access[0], new_word, access[2]))

# 8
attempts = ("success", "fail", "fail", "success", "fail", "fail")
print("Успехов:", attempts.count("success"))
print("Неудач:", attempts.count("fail"))

# 9
admins = ("root", "admin")
users_list = ("alex", "bob")
print("Общий список:", admins + users_list)

# 10
logs = ("login", "upload", "download", "logout")
start = logs[0]
middle = logs[1:-1]
end = logs[-1]
print("Начало:", start)
print("Середина:", middle)
print("Конец:", end)
