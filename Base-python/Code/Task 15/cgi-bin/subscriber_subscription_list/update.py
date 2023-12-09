
#!/usr/bin/env python3

print("Content-Type: text/html;charset=utf-8\n")

import cgi
import cgitb
import sqlite3
import html

cgitb.enable()

message = ""

def changeData(con):
    global message
    cursorObj = con.cursor()
    form = cgi.FieldStorage()

    subscribers_subscriptions_id = form.getfirst("subscribers_subscriptions_id", "-default-")
    user_id = form.getfirst("user_id", "-default-")
    community_id = form.getfirst("community_id", "-default-")

    subscribers_subscriptions_id = html.escape(subscribers_subscriptions_id)
    user_id = html.escape(user_id)
    community_id = html.escape(community_id)

    if subscribers_subscriptions_id != "-default-" or user_id != "-default-" or community_id != "-default-":
        temp_list = []
        temp_list.append(user_id)
        temp_list.append(community_id)
        temp_list.append(subscribers_subscriptions_id)

        cursorObj.execute(
            "UPDATE subscriber_subscription_list SET user_id = ?, community_id = ? WHERE subscribers_subscriptions_id = ?",
            temp_list)
        message = f"<p>Запись с Id  '{subscribers_subscriptions_id}' была изменена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
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

def showById(con):
    global message
    result = []
    cursorObj = con.cursor()
    form = cgi.FieldStorage()

    id = form.getfirst("surname", "-default-")
    id = html.escape(id)
    if id == "-default-":
        cursorObj.execute("SELECT FROM communities WHERE id_worker = " + id + ";")
        con.commit()
        result = cursorObj.fetchall()
    return result

con = sqlite3.connect("NEAR.db")
changeData(con)
con.close()
