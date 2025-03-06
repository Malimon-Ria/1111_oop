import sqlite3

connection = sqlite3.connect("EXAM.sl3", timeout=5)
cur = connection.cursor()

# ======= CREATE TABLE =========
#cur.execute("CREATE TABLE users (login TEXT UNIQUE, password TEXT, phone TEXT);")
#connection.commit()

choice = input("1-Реєстрація, 2-Вхід ")

# ======== INSERT ==========
if choice == "1":
    login = input("Логін:")
    password = input("Пароль:")
    phone = input("Телефон:")
    try:
        cur.execute(f"INSERT INTO users (login, password, phone) VALUES ('{login}', '{password}', '{phone}');")
        connection.commit()
        print("Реєстраціч успішна!")
    except sqlite3.IntegrityError:
        print("Логін існує!")

elif choice == "2":
    login = input("Логін:")
    password = input("Пароль:")
    cur.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{password}'")
    res = cur.fetchone()
    if res:
        print("Вітаю ви увійшли!")
    else:
        print("Невірний логін або пароль!")

connection.close()
