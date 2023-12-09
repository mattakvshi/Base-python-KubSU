
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

    user_id = form.getfirst("user_id", "-default-")
    first_name = form.getfirst("first_name", "-default-")
    last_name = form.getfirst("last_name", "-default-")
    birthday = form.getfirst("birthday", "-default-")
    user_age = form.getfirst("user_age", "-default-")
    registration_date = form.getfirst("registration_date", "-default-")
    country = form.getfirst("country", "-default-")
    city = form.getfirst("city", "-default-")
    district = form.getfirst("district", "-default-")

    user_id = html.escape(user_id)
    first_name = html.escape(first_name)
    last_name = html.escape(last_name)
    birthday = html.escape(birthday)
    user_age = html.escape(user_age)
    registration_date = html.escape(registration_date)
    country = html.escape(country)
    city = html.escape(city)
    district = html.escape(district)



    if user_id != "-default-" or first_name == "-default-" or last_name == "-default-" or birthday == "-default-" or user_age == "-default-" or registration_date == "-default-" or country == "-default-" or city == "-default-" or district == "-default-":
        temp_list = []

        temp_list.append(first_name)
        temp_list.append(last_name)
        temp_list.append(birthday)
        temp_list.append(user_age)
        temp_list.append(registration_date)
        temp_list.append(country)
        temp_list.append(city)
        temp_list.append(district)
        temp_list.append(user_id)

        cursorObj.execute(
            "UPDATE user SET first_name = ?, last_name = ?, birthday = ?, user_age = ?, registration_date = ?, country = ?, city = ?, district = ? WHERE user_id = ?",
            temp_list)
        message = f"<p>Пользователь с Id = '{user_id}' был изменён.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица User</title>
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

    id = form.getfirst("user_id", "-default-")
    id = html.escape(id)
    if id == "-default-":
        cursorObj.execute("SELECT FROM communities WHERE id_worker = " + id + ";")
        con.commit()
        result = cursorObj.fetchall()
    return result

con = sqlite3.connect("NEAR.db")
changeData(con)
con.close()
