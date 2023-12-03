
#!/usr/bin/env python3

print("Content-Type: text/html;charset=utf-8\n")

import cgitb
import sqlite3

cgitb.enable()

def showData(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Teachers")
    result = "\n".join(str(row) for row in cursorObj.fetchall())
    pattern = """
    <!DOCTYPE html>
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

            textarea
            {{
                resize: none;
                width: 800px;
                height: 450px;
            }}

            .buttonWrapper
            {{
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <div>
            <h1>Окно вывода данных таблицы</h1>
        </div>
        <div>
            <textarea>{}</textarea>
        </div>
        <div class = "buttonWrapper" style = "margin-right: 200px;">
            <a href = "http://localhost:8080/Main.html"><button>Назад</button></a>
        </div>
        <div class = "buttonWrapper">
            <p>Другие действия с этой же таблицей</p>
            <a href = "http://localhost:8080/Forms_Teachers/FormTeachersInsert.html"><button>Вставить данные</button></a>
            <a href = "http://localhost:8080/Forms_Teachers/FormTeachersShow.html"><button>Показать данные ещё раз</button></a>
            <a href = "http://localhost:8080/Forms_Teachers/FormTeachersChange.html"><button>Изменить данные</button></a>
        </div>
    </body>
</html>"""
    print(pattern.format(result))
    con.commit()

con = sqlite3.connect("D:/Programming/Python/Interpreted_Programming_Languages/Work_14/ComputerClassesDB.db")
showData(con)
con.close()
