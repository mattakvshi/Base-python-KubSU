
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
    nameSubject = form.getfirst("NameSubject", "-default-")
    id = html.escape(id)
    nameSubject = html.escape(nameSubject)
    if id != "-default-" and nameSubject != "-default-":
        temp_list = []
        temp_list.append(nameSubject)
        temp_list.append(id)
        cursorObj.execute("UPDATE Subjects SET NameSubject = ? WHERE Id = ?", temp_list)
        message = f"<p>Запись с Id  '{id}' была изменена на '{nameSubject}'.</p>"
    elif id != "-default-" and nameSubject == "-default-":
        cursorObj.execute("DELETE FROM Subjects WHERE Id = ?", (id,))
        message = f"<p>Запись с Id  '{id}' была удалена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите данные.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Subjects</title>
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
                <a href = "http://localhost:8080/Forms_Subjects/FormSubjectsShow.html"><button>Показать данные</button></a>
                <a href = "http://localhost:8080/Forms_Subjects/FormSubjectsChange.html"><button>Изменить данные ещё раз</button></a>
                <a href = "http://localhost:8080/Forms_Subjects/FormSubjectsInsert.html"><button>Вставить данные</button></a>
            </div>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("D:/Programming/Python/Interpreted_Programming_Languages/Work_14/ComputerClassesDB.db")
changeData(con)
con.close()
