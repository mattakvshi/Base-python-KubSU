
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
    id = form.getfirst("Id", "-default-")
    surnameListener = form.getfirst("SurnameListener", "-default-")
    nameListener = form.getfirst("NameListener", "-default-")
    patronymicListener = form.getfirst("PatronymicListener", "-default-")
    idListener = form.getfirst("IdListener", "-default-")
    id = html.escape(id)
    surnameListener = html.escape(surnameListener)
    nameListener = html.escape(nameListener)
    patronymicListener = html.escape(patronymicListener)
    idListener = html.escape(idListener)
    if id != "-default-" and surnameListener != "-default-" and nameListener != "-default-" and patronymicListener != "-default-" and idListener != "-default-":
        temp_list = []
        temp_list.append(surnameListener)
        temp_list.append(nameListener)
        temp_list.append(patronymicListener)
        temp_list.append(idListener)
        temp_list.append(id)
        cursorObj.execute(
            "UPDATE Group1 SET SurnameListener = ?, NameListener = ?, PatronymicListener = ?, IdSubject = ? WHERE Id = ?",
            temp_list)
        message = f"<p>Запись с Id  '{id}' была изменена.</p>"
    elif id != "-default-" and surnameListener == "-default-" and nameListener == "-default-" and patronymicListener == "-default-" and idListener == "-default-":
        cursorObj.execute("DELETE FROM Group1 WHERE Id = ?", (id,))
        message = f"<p>Запись с Id  '{id}' была удалена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Group1</title>
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
        <div>
            <div class = "buttonWrapper" style = "margin-right: 200px;">
                <a href = "http://localhost:8080/Main.html"><button>Назад</button></a>
            </div>
            <div class = "buttonWrapper">
                <p>Другие действия с этой же таблицей</p>
                <a href = "http://localhost:8080/Forms_Group1/FormGroup1Show.html"><button>Показать данные</button></a>
                <a href = "http://localhost:8080/Forms_Group1/FormGroup1Change.html"><button>Изменить данные ещё раз</button></a>
                <a href = "http://localhost:8080/Forms_Group1/FormGroup1Insert.html"><button>Вставить данные</button></a>
            </div>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("D:/Programming/Python/Interpreted_Programming_Languages/Work_14/ComputerClassesDB.db")
changeData(con)
con.close()
