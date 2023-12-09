#!/usr/bin/env python3

import cgitb
import sqlite3

print("Content-Type: text/html;charset=utf-8\n")

cgitb.enable()

def showData(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Community")
    rows = cursorObj.fetchall()
    table_rows = ""
    for row in rows:
        table_rows += f"""
        <tr class="w-75" style="background-color: #D2D2D2;">
            <th scope="row" style="background-color: #D2D2D2;">{row[0]}</th>
            <td style="background-color: #D2D2D2;">{row[1]}</td>
            <td style="background-color: #D2D2D2;">{row[2]}</td>
            <td style="background-color: #D2D2D2;">{row[3]}</td>
            <td style="background-color: #D2D2D2;">{row[4]}</td>
            <td style="background-color: #D2D2D2;">{row[5]}</td>
        </tr>
        """

    pattern = f"""<!DOCTYPE html>
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
        <div class = "container text-center">
            <h1 class="display-6 mb-5"><strong>Окно вывода данных о сообществах</strong></h1>
        </div>
        <div class="d-flex justify-content-center">
        <div class="w-75 text-center" style="background-color: #D2D2D2;">
            <table class="table table-bordered border-primary" style="border-color: #FF4C2B;">
                <thead style="border-color: #FF4C2B;>
                    <tr style="border-color: #FF4C2B;">
                        <th scope="row" style="border-color: #FF4C2B;">community_id</th>
                        <th scope="row" style="border-color: #FF4C2B;">community_name</th>
                        <th scope="row" style="border-color: #FF4C2B;">community_description</th>
                        <th scope="row" style="border-color: #FF4C2B;">country</th>
                        <th scope="row" style="border-color: #FF4C2B;">city</th>
                        <th scope="row" style="border-color: #FF4C2B;">district</th>
                    </tr>
                </thead style="border-color: #FF4C2B; background-color: #D2D2D2;">
                <tbody style="border-color: #FF4C2B; background-color: #D2D2D2;">
                {table_rows}
                </tbody>
            </table>
        </div>
        </div>
    </body>
</html>"""
    print(pattern)
    con.commit()

con = sqlite3.connect("NEAR.db")
showData(con)
con.close()