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

    community_name = form.getfirst("community_name", "-default-")
    community_description = form.getfirst("community_description", "-default-")
    country = form.getfirst("country", "-default-")
    city = form.getfirst("city", "-default-")
    district = form.getfirst("district", "-default-")

    community_name = html.escape(community_name)
    community_description = html.escape(community_description)
    country = html.escape(country)
    city = html.escape(city)
    district = html.escape(district)

    temp_list = []

    temp_list.append(community_name)
    temp_list.append(community_description)
    temp_list.append(country)
    temp_list.append(city)
    temp_list.append(district)

    if community_name == "-default-" or community_description == "-default-" or country == "-default-" or city == "-default-" or district == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO Community(community_name, community_description, country, city, district) VALUES(?, ?, ?, ?, ?)", temp_list)
        message = f"<p>Сообщество '{community_name, community_description, country, city, district}' успешно добавлено в базу данных.</p>"
    pattern = """<!DOCTYPE html>
    <html lang = "ru">
        <head>
            <meta charset = "UTF-8">
            <title>Таблица communities</title>
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