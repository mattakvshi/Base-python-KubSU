#!/usr/bin/env python3

print("Content-Type: text/html;charset=utf-8\n")

import cgi
import cgitb
import sqlite3
import html

cgitb.enable()

message = ""

def insertData(con):
    global message
    cursorObj = con.cursor()
    form = cgi.FieldStorage()
    user_id = form.getfirst("user_id", "-default-")
    community_id = form.getfirst("community_id", "-default-")
    user_id = html.escape(user_id)
    community_id = html.escape(community_id)
    temp_list = []
    temp_list.append(user_id)
    temp_list.append(community_id)
    if user_id == "-default-" or community_id == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO subscriber_subscription_list(user_id, community_id) VALUES(?, ?)", temp_list)
        message = f"<p>Запись '{user_id, community_id}' успешно добавлена в базу данных.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица subscriber_subscription_list</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body style="background-color: #D2D2D2; color: #0A1F32;">
        <div class="col mt-4 ms-4">
            <a href = "http://localhost:8000/index.html"><button class="btn btn-primary" style="color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;">Назад</button></a>
        </div>
        <div class=" w-100 position-fixed top-50 d-flex justify-content-center align-items-center" style="font-size: 30px; font-weight: 500;">
            {}
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("NEAR.db")
insertData(con)
con.close()