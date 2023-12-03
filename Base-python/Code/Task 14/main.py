import sqlite3
from sqlite3 import Error
import random


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                birthday DATE,
                user_age INTEGER,
                registration_date DATE NOT NULL,
                country TEXT,
                city TEXT,
                district TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Community (
                community_id INTEGER PRIMARY KEY AUTOINCREMENT,
                community_name TEXT NOT NULL,
                community_description TEXT NOT NULL,
                country TEXT,
                city TEXT,
                district TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Authorization_data (
                authorization_data_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                user_email TEXT NOT NULL,
                encoded_user_password TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(user_id)
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Community_authorization_data (
                community_authorization_data_id INTEGER PRIMARY KEY AUTOINCREMENT,
                community_id INTEGER NOT NULL,
                community_email TEXT NOT NULL,
                community_encoded_password TEXT NOT NULL,
                FOREIGN KEY (community_id) REFERENCES Community(community_id)
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Notification_options (
                option_id INTEGER PRIMARY KEY AUTOINCREMENT,
                option_name TEXT NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Notification_options_Users (
                notification_option_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                option_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(user_id),
                FOREIGN KEY (option_id) REFERENCES Notification_options(option_id)
            )
        ''')


    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Monitored_emergency (
                emergency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                emergency_name TEXT NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Monitored_emergency_Community (
                monitoring_option_id INTEGER PRIMARY KEY AUTOINCREMENT,
                community_id INTEGER NOT NULL,
                emergency_id INTEGER NOT NULL,
                FOREIGN KEY (community_id) REFERENCES Community(community_id),
                FOREIGN KEY (emergency_id) REFERENCES Monitored_emergency(emergency_id)
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Subscriber_subscription_list (
                subscribers_subscriptions_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                community_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(user_id),
                FOREIGN KEY (community_id) REFERENCES Community(community_id)
            )
        ''')

    connection.commit()


def fill_tables(connection):
    cursor = connection.cursor()

    # Заполнение таблицы User
    cursor.execute(
        "INSERT INTO User (first_name, last_name, birthday, user_age, registration_date, country, city, district) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        ("John", "Doe", "1990-01-01", 32, "2023-01-01", "USA", "New York", "Manhattan"))

    # Повторите оператор INSERT для добавления 9 других записей
    data = [
        ("Alice", "Johnson", "1985-05-15", 36, "2022-12-01", "Canada", "Toronto", "Downtown"),
        ("Bob", "Smith", "1988-07-20", 33, "2022-11-15", "UK", "London", "Westminster"),
        ("Eva", "Brown", "1995-03-10", 28, "2023-02-05", "Germany", "Berlin", "Mitte"),
        ("Chris", "Miller", "1992-09-18", 31, "2022-10-10", "Australia", "Sydney", "CBD"),
        ("Sophia", "Williams", "1980-12-05", 41, "2023-03-20", "USA", "Los Angeles", "Hollywood"),
        ("David", "Taylor", "1983-04-25", 38, "2023-04-15", "Canada", "Vancouver", "Downtown"),
        ("Emma", "Anderson", "1998-06-30", 25, "2022-09-01", "UK", "Manchester", "City Center"),
        ("Michael", "Clark", "1991-11-08", 30, "2022-08-10", "Germany", "Hamburg", "St. Pauli"),
        ("Olivia", "Moore", "1987-02-14", 34, "2023-05-12", "Australia", "Melbourne", "CBD")
    ]

    for record in data:
        cursor.execute(
            "INSERT INTO User (first_name, last_name, birthday, user_age, registration_date, country, city, district) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            record)

    # Заполнение таблицы Community
    cursor.execute("INSERT INTO Community (community_name, community_description, country, city, district) VALUES (?, ?, ?, ?, ?)",
                   ("Community A", "Description A", "USA", "Los Angeles", "Downtown"))

    data_community = [
        ("Community B", "Description B", "Canada", "Toronto", "Downtown"),
        ("Community C", "Description C", "UK", "London", "Westminster"),
        ("Community D", "Description D", "Germany", "Berlin", "Mitte"),
        ("Community E", "Description E", "Australia", "Sydney", "CBD"),
        ("Community F", "Description F", "USA", "New York", "Manhattan"),
        ("Community G", "Description G", "Canada", "Vancouver", "Downtown"),
        ("Community H", "Description H", "UK", "Manchester", "City Center"),
        ("Community I", "Description I", "Germany", "Hamburg", "St. Pauli"),
        ("Community J", "Description J", "Australia", "Melbourne", "CBD")
    ]

    for record in data_community:
        cursor.execute(
            "INSERT INTO Community (community_name, community_description, country, city, district) VALUES (?, ?, ?, ?, ?)",
            record)

    # Заполнение таблицы Authorization_data
    cursor.execute("INSERT INTO Authorization_data (user_id, user_email, encoded_user_password) VALUES (?, ?, ?)",
                   (1, "john.doe@example.com", "435kl6hlk345j6"))

    data_authorization = [
        (2, "alice.johnson@example.com", "34j6hlk6bnkj5"),
        (3, "bob.smith@example.com", "gje256wro985g20"),
        (4, "eva.brown@example.com", "j6h34o5li6uh"),
        (5, "chris.miller@example.com", "243k56ojp324i57"),
        (6, "sophia.williams@example.com", "6435hjjh34ihio"),
        (7, "david.taylor@example.com", "lh435645injmpo"),
        (8, "emma.anderson@example.com", "435oihjno45"),
        (9, "michael.clark@example.com", "34twerfgh46t3"),
        (10, "olivia.moore@example.com", "43ghert45yhrt")
    ]

    for record in data_authorization:
        cursor.execute("INSERT INTO Authorization_data (user_id, user_email, encoded_user_password) VALUES (?, ?, ?)",
                       record)

    # Заполнение таблицы Community_authorization_data
    cursor.execute("INSERT INTO Community_authorization_data (community_id, community_email, community_encoded_password) VALUES (?, ?, ?)",
                   (1, "communityA@example.com", "hashed_password"))

    data_community_auth = [
        (2, "communityB@example.com", "hashed_password"),
        (3, "communityC@example.com", "hashed_password"),
        (4, "communityD@example.com", "hashed_password"),
        (5, "communityE@example.com", "hashed_password"),
        (6, "communityF@example.com", "hashed_password"),
        (7, "communityG@example.com", "hashed_password"),
        (8, "communityH@example.com", "hashed_password"),
        (9, "communityI@example.com", "hashed_password"),
        (10, "communityJ@example.com", "hashed_password")
    ]

    for record in data_community_auth:
        cursor.execute(
            "INSERT INTO Community_authorization_data (community_id, community_email, community_encoded_password) VALUES (?, ?, ?)",
            record)

        # Заполнение таблицы Notification_options
        cursor.execute("INSERT INTO Notification_options (option_name) VALUES (?)",
                       ("Telegram",))

        data_notification_options = [
            ("Email",),
            ("Push-notification",)
        ]

        cursor.executemany("INSERT INTO Notification_options (option_name) VALUES (?)", data_notification_options)

    # Заполнение таблицы Notification_options_Users
    cursor.execute("INSERT INTO Notification_options_Users (user_id, option_id) VALUES (?, ?)",
                   (1, 1))

    data_notification_users = [
        (2, 2),
        (3, 3),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 1),
        (8, 2),
        (9, 3),
        (10, 1)
    ]

    for record in data_notification_users:
        cursor.execute("INSERT INTO Notification_options_Users (user_id, option_id) VALUES (?, ?)",
                       record)

        # Заполнение таблицы Monitored_emergency
        cursor.execute("INSERT INTO Monitored_emergency (emergency_name) VALUES (?)",
                       ("Earthquake",))

        data_monitored_emergency = [
            ("Forest fires",),
            ("Flood",),
            ("Terrorist attack",),
            ("Other",)
        ]


        cursor.executemany("INSERT INTO Monitored_emergency (emergency_name) VALUES (?)", data_monitored_emergency)


    # Заполнение таблицы Monitored_emergency_Community
    cursor.execute("INSERT INTO Monitored_emergency_Community (community_id, emergency_id) VALUES (?, ?)",
                   (1, 1))

    data_monitored_emergency_community = [
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 1),
        (7, 2),
        (8, 3),
        (9, 4),
        (10, 5)
    ]

    for record in data_monitored_emergency_community:
        cursor.execute("INSERT INTO Monitored_emergency_Community (community_id, emergency_id) VALUES (?, ?)",
                       record)


    # Заполнение таблицы Subscriber_subscription_list
    cursor.execute("INSERT INTO Subscriber_subscription_list (user_id, community_id) VALUES (?, ?)",
                   (1, 1))

    data_subscriber_subscription = [
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    ]

    for record in data_subscriber_subscription:
        cursor.execute("INSERT INTO Subscriber_subscription_list (user_id, community_id) VALUES (?, ?)",
                       record)

    connection.commit()


def execute_queries(connection):
    cursor = connection.cursor()

    # Пример выполнения запросов

    # Выборка первых 10 записей из таблицы User
    cursor.execute("SELECT * FROM User LIMIT 10")
    rows = cursor.fetchall()

    print("Первые десять записей из таблицы User:")
    for row in rows:
        print(
            f"User ID: {row[0]}, Name: {row[1]} {row[2]}, Birthday: {row[3]}, Age: {row[4]}, Registration Date: {row[5]}, Country: {row[6]}, City: {row[7]}, District: {row[8]}")

    #  Выбрать название и описание всех сообществ в Германии
    cursor.execute("SELECT community_name, community_description FROM Community WHERE country = 'Germany'")
    rows = cursor.fetchall()
    print("\nНазвание и описание сообществ в Германии:")
    for row in rows:
        print(f"Community Name: {row[0]}, Description: {row[1]}")

    #  Подсчитать количество пользователей в каждом сообществе
    cursor.execute("SELECT community_id, COUNT(user_id) FROM Subscriber_subscription_list GROUP BY community_id")
    rows = cursor.fetchall()
    print("\nКоличество пользователей в каждом сообществе:")
    for row in rows:
        print(f"Community ID: {row[0]}, Number of Users: {row[1]}")

    # Найти пользователя с самым ранним днем рождения
    cursor.execute("SELECT * FROM User ORDER BY birthday ASC LIMIT 1")
    row = cursor.fetchone()
    print("\nПользователь с самым ранним днем рождения:")
    print(
        f"User ID: {row[0]}, Name: {row[1]} {row[2]}, Birthday: {row[3]}, Age: {row[4]}, Registration Date: {row[5]}, Country: {row[6]}, City: {row[7]}, District: {row[8]}")
    print("\n")

    # Получение списка сообществ и числа пользователей в каждом сообществе
    cursor.execute("SELECT Community.community_name, COUNT(User.user_id) AS user_count "
                   "FROM Community JOIN Subscriber_subscription_list ON Community.community_id = Subscriber_subscription_list.community_id "
                   "JOIN User ON Subscriber_subscription_list.user_id = User.user_id "
                   "GROUP BY Community.community_id")
    print("Сообщества и число пользователей в каждом сообществе:")
    print(cursor.fetchall())
    print("\n")

    # Получение информации о пользователях, подписанных на push-уведомления
    cursor.execute("SELECT User.user_id, first_name, last_name FROM User "
                   "JOIN Notification_options_Users ON User.user_id = Notification_options_Users.user_id "
                   "WHERE option_id = 2")
    print("Пользователи, подписанные на push-уведомления:")
    print(cursor.fetchall())
    print("\n")

    # Получение списка сообществ, в которых есть уведомление по email
    cursor.execute(
        "SELECT * FROM Community WHERE community_id IN (SELECT community_id FROM Notification_options_Users WHERE option_id = 1)")
    print("Сообщества с уведомлением по email:")
    print(cursor.fetchall())
    print("\n")

    # Получение информации о пользователях старше 30 лет
    cursor.execute("SELECT * FROM User WHERE user_age > 30")
    print("Пользователи старше 30 лет:")
    print(cursor.fetchall())
    print("\n")

    # Обновление первых 10 записей в таблице Community
    cursor.execute(
        "UPDATE Community SET community_name = 'Updated' WHERE community_id IN (SELECT community_id FROM Community LIMIT 10)")

    cursor.execute(
        "SELECT * FROM Community  WHERE community_id IN (SELECT community_id FROM Community LIMIT 10)")
    print("Названия сообществ после обновления: ")
    print(cursor.fetchall())
    print("\n")

    # Удаление первых 10 записей из таблицы Authorization_data
    cursor.execute(
        "DELETE FROM Authorization_data WHERE authorization_data_id IN (SELECT authorization_data_id FROM Authorization_data LIMIT 10)")

    cursor.execute(
        "SELECT * FROM Authorization_data WHERE authorization_data_id IN (SELECT authorization_data_id FROM Authorization_data LIMIT 10)")
    print("Данные для авторизации после удаления: ")
    print(cursor.fetchall())
    print("\n")

    connection.commit()


def sql_connection():
    try:
        con = sqlite3.connect("NEAR.db")
        con.execute("PRAGMA foreign_keys = ON")
        return con
    except Error:
        print(Error)


con = sql_connection()
create_tables(con)
fill_tables(con)
execute_queries(con)

con.close()
