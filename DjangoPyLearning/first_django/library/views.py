from django.shortcuts import render
import pymysql


def main_page_library(request):
    result = None
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="library",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected")
        try:
            while True:
                with connection.cursor() as cursor:
                    data = f"select * from library"
                    cursor.execute(data)
                    result = cursor.fetchall()
        finally:
            connection.close()

    except:
        print("Error")

    return render(request, 'library/library_main_page.html', {"result": result})
