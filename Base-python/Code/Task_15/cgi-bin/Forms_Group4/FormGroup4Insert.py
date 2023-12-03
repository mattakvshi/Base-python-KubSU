
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
    surnameListener = form.getfirst("SurnameListener", "-default-")
    nameListener = form.getfirst("NameListener", "-default-")
    patronymicListener = form.getfirst("PatronymicListener", "-default-")
    idListener = form.getfirst("IdListener", "-default-")
    surnameListener = html.escape(surnameListener)
    nameListener = html.escape(nameListener)
    patronymicListener = html.escape(patronymicListener)
    idListener = html.escape(idListener)
    temp_list = []
    temp_list.append(surnameListener)
    temp_list.append(nameListener)
    temp_list.append(patronymicListener)
    temp_list.append(idListener)
    if surnameListener == "-default-" or nameListener == "-default-" or patronymicListener == "-default-" or idListener == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO Group4(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES(?, ?, ?, ?)", temp_list)
        message = f"<p>Участник группы '{surnameListener, nameListener, patronymicListener, idListener}' успешно добавлен в базу данных.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Group4</title>
        <style>
            body
                {{
                    font-family: Microsoft YaHei UI, sans-serif;
                    color: rgb(130, 130, 130);
                    text-align: center;
                }}

                button, input
                {{
                    color: rgb(0, 165, 80);
                }}

                button:hover, input:hover
                {{
                    transform: scale(1.1);
                }}

                .buttonWrapper
                {{
                    display: inline-block;
                }}
        </style>
    </head>
    <body>
        <div>
            {}
        </div>
        <div class = "buttonWrapper" style = "margin-right: 100px;">
            <a href = "http://localhost:8080/Main.html"><button>Назад</button></a>
        </div>
        <div class = "buttonWrapper">
            <p>Другие действия с этой же таблицей</p>
            <a href = "http://localhost:8080/Forms_Group4/FormGroup4Show.html"><button>Показать данные</button></a>
            <a href = "http://localhost:8080/Forms_Group4/FormGroup4Insert.html"><button>Вставить данные ещё раз</button></a>
            <a href = "http://localhost:8080/Forms_Group4/FormGroup4Change.html"><button>Изменить данные</button></a>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("D:/Programming/Python/Interpreted_Programming_Languages/Work_14/ComputerClassesDB.db")
insertData(con)
con.close()
