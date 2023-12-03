
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
    surnameTeacher = form.getfirst("SurnameTeacher", "-default-")
    nameTeacher = form.getfirst("NameTeacher", "-default-")
    patronymicTeacher = form.getfirst("PatronymicTeacher", "-default-")
    idSubject = form.getfirst("IdSubject", "-default-")
    id = html.escape(id)
    surnameTeacher = html.escape(surnameTeacher)
    nameTeacher = html.escape(nameTeacher)
    patronymicTeacher = html.escape(patronymicTeacher)
    idSubject = html.escape(idSubject)
    if id != "-default-" and surnameTeacher != "-default-" and nameTeacher != "-default-" and patronymicTeacher != "-default-" and idSubject != "-default-":
        temp_list = []
        temp_list.append(surnameTeacher)
        temp_list.append(nameTeacher)
        temp_list.append(patronymicTeacher)
        temp_list.append(idSubject)
        temp_list.append(id)
        cursorObj.execute("UPDATE Teachers SET SurnameTeacher = ?, NameTeacher = ?, PatronymicTeacher = ?, IdSubject = ? WHERE Id = ?", temp_list)
        message = f"<p>Запись с Id  '{id}' была изменена.</p>"
    elif id != "-default-" and surnameTeacher == "-default-" and nameTeacher == "-default-" and patronymicTeacher == "-default-" and idSubject == "-default-":
        cursorObj.execute("DELETE FROM Teachers WHERE Id = ?", (id,))
        message = f"<p>Запись с Id  '{id}' была удалена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Teachers</title>
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
            <div class = "buttonWrapper" style = "margin-right: 200px;">
                <a href = "http://localhost:8080/Main.html"><button>Назад</button></a>
            </div>
            <div class = "buttonWrapper">
                <p>Другие действия с этой же таблицей</p>
                <a href = "http://localhost:8080/Forms_Teachers/FormTeachersShow.html"><button>Показать данные</button></a>
                <a href = "http://localhost:8080/Forms_Teachers/FormTeachersChange.html"><button>Изменить данные ещё раз</button></a>
                <a href = "http://localhost:8080/Forms_Teachers/FormTeachersInsert.html"><button>Вставить данные</button></a>
            </div>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("D:/Programming/Python/Interpreted_Programming_Languages/Work_14/ComputerClassesDB.db")
changeData(con)
con.close()
