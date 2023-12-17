
import re
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.apps import apps
from .models import *
import hashlib
import random


def search_email(input_email):
    users = Users.objects.filter(email=input_email)
    if not users:
        return True
    else:
        return False


def checking_for_availability(input_email, input_password):
    user = Users.objects.filter(email=input_email, password=input_password)
    if not user:
        return False
    else:
        return True


def get_user(input_email):
    user = Users.objects.get(email=input_email)
    return user


def sign_up(request):
    return render(request, "sign_up/sign_up.html")


def sign_up_sending(request):
    surname = request.POST.get("surname", "-undefined-")
    name = request.POST.get("name", "-undefined-")
    patronymic = request.POST.get("patronymic", "-undefined-")
    email = request.POST.get("email", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    name_regex = r"^([А-ЯЁ][а-яё]+)$"
    email_regex = r"^[^@]+@[^@]+\.[a-zA-Z]{2,5}$"
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{8,}$"

    error_surname, error_name, error_patronymic, error_email, error_password = '', '', '', '', ''
    kol = 0

    if not re.match(name_regex, surname):
        error_surname = f'''
                <div class="pass-row">
                    <input name="surname" type="text" style="border: 3px solid red;" value="{surname}">
                    <button class="eye btn btn-primary" style="pointer-events: none; font-size: 30px; color: #D2D2D2; background-color: #D2D2D2; border-color: #D2D2D2;" type="button">👁</button>
                </div>
                <p style="font-size: 9px;">Фамилия должна начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>
                '''
        kol += 1
    else:
        error_surname = f'<input name="surname" type="text" value="{surname}">'
    if not re.match(name_regex, name):
        error_name = f'''
                <div class="pass-row">
                    <input name="name" type="text" style="border: 3px solid red;" value="{name}">
                    <button class="eye btn btn-primary" style="pointer-events: none; font-size: 30px; color: #D2D2D2; background-color: #D2D2D2; border-color: #D2D2D2;" type="button">👁</button>
                </div>
                <p style="font-size: 9px;">Имя должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
        kol += 1
    else:
        error_name = f'<input name="name" type="text" value="{name}">'
    if not re.match(name_regex, patronymic):
        error_patronymic = f'''
                <div class="pass-row">
                    <input name="patronymic" type="text" style="border: 3px solid red;" value="{patronymic}">
                    <button class="eye btn btn-primary" style="pointer-events: none; font-size: 30px; color: #D2D2D2; background-color: #D2D2D2; border-color: #D2D2D2;" type="button">👁</button>
                </div>
                <p style="font-size: 9px;">Отчество должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
        kol += 1
    else:
        error_patronymic = f'<input name="patronymic" type="text" value="{patronymic}">'
    if not re.match(email_regex, email):
        error_email = f'''
                <div class="pass-row">
                    <input name="email" type="email" style="border: 3px solid red;" value="{email}">
                    <button class="eye btn btn-primary" style="pointer-events: none; font-size: 30px; color: #D2D2D2; background-color: #D2D2D2; border-color: #D2D2D2;" type="button">👁</button>
                </div>
                <p style="font-size: 9px;">Почта должна быть в виде login@email.domain</p>'''
        kol += 1
    else:
        error_email = f'<input name="email" type="email" value="{email}">'
    if not re.match(password_regex, password):
        error_password = f'''
                <div class="pass-row">
                    <input id="passwordInput" name="password" type="password" style="border: 3px solid red;" value="{password}">
                    <button id="toggleButton" class="eye btn btn-primary" style=" font-size: 30px; color: #D2D2D2; background-color: #344756; border-color: #344756;" type="button">👁</button>
                </div>
                <p style="font-size: 9px;">Пароль должен содержать заглавные и строчные латинские буквы, специальные символы и быть не менее 8 символов </p>'''
        kol += 1
    else:
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'

    if kol == 0:
        if search_email(email):
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            user = Users(
                type="Default_User",
                surname=surname,
                name=name,
                patronymic=patronymic,
                email=email,
                password=md5.hexdigest()
            )
            user.save()
            request.session["user_email"] = email
            messages.success(request, "Вы успешно зарегистрировались!")
            data = {"error_surname": error_surname, "error_name": error_name,
                    "error_patronymic": error_patronymic, "error_email": error_email,
                    "error_password": error_password}
            return render(request, "sign_up/redirect_s.html", context=data)
        else:
            messages.error(request, "Пользователь с такой почтой уже существует!")
            data = {"error_surname": error_surname, "error_name": error_name,
                    "error_patronymic": error_patronymic, "error_email": error_email,
                    "error_password": error_password}
            return render(request, "sign_up/sign_up_sending.html", context=data)

    data = {"error_surname": error_surname, "error_name": error_name,
            "error_patronymic": error_patronymic, "error_email": error_email,
            "error_password": error_password}
    return render(request, "sign_up/sign_up_sending.html", context=data)


def log_in(request):
    return render(request, "log_in/log_in.html")


def log_in_sending(request):
    email = request.POST.get("email", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    error_email, error_password = '', ''

    error_email = f'<input name="email" type="email" value="{email}">'
    error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if checking_for_availability(email, md5.hexdigest()):
        request.session["user_email"] = email
        messages.success(request, "Вы успешно авторизовались!")
        data = {"error_email": error_email, "error_password": error_password}
        return render(request, "log_in/redirect_l.html", context=data)
    else:
        messages.error(request, "Вы ввели неверную почту/пароль!")
        data = {"error_email": error_email, "error_password": error_password}
        return render(request, "log_in/log_in_sending.html", context=data)


def password_recovery(request):
    return render(request, "password_recovery/password_recovery.html")


def password_recovery_sending(request):
    email = request.POST.get("email", "-undefined-")
    error_email = f'<input name="email" type="email" value="{email}">'
    input_code = request.POST.get("code", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    code = request.session.get('code', ''.join(random.choices("0123456789", k=7)))

    if search_email(email) and input_code == "" and password == "":
        error_code = f'<input name="code" type="text" value="{input_code}">'
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        messages.error(request, "Вы ввели неверную почту!")
        button_code = f'<button type="submit">Отправить код</button>'
        button_submit = f'<button type="button">Поменять пароль</button>'
        data = {"error_email": error_email, "button_code": button_code, "error_code": error_code,
                "error_password": error_password, "button_submit": button_submit}
        return render(request, "password_recovery/password_recovery_sending.html", context=data)
    else:
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{8,}$"
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        button_code = f'<button type="button">Отправить код</button>'
        button_submit = f'<button type="submit">Поменять пароль</button>'
        error_code = f'<input name="code" type="text" value="{input_code}">'

        if not search_email(email) and input_code == "" and password == "":
            subject = "Восстановление пароля"
            output_message = f"Ваш код для восстановления пароля: {code}"
            from_email = "anton-ivanov-080203@mail.ru"
            send_mail(subject, output_message, from_email, [email])
            messages.success(request, "Код отправлен на вашу почту!")
            request.session['code'] = code
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "error_password": error_password, "button_submit": button_submit}
            return render(request, "password_recovery/password_recovery_sending.html", context=data)

        kol = 0
        if not re.match(password_regex, password):
            error_password = f'''
                    <input id="passwordInput" name="password" type="password" style="border: 3px solid red;" value="{password}">
                    <p style="font-size: 9px;">Пароль должен содержать заглавные и строчные латинские буквы, специальные символы и быть не менее 8 символов </p>'''
            kol += 1
        else:
            error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        if str(input_code) != str(code):
            error_code = f'<input name="code" type="text" value="{input_code}" style="border: 3px solid red;">'
            kol += 1
        else:
            error_code = f'<input name="code" type="text" value="{input_code}">'

        if kol == 0:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            user = get_user(email)
            user.password = md5.hexdigest()
            user.save()
            request.session["user_email"] = email
            messages.success(request, "Вы успешно сменили пароль!")
            del request.session['code']
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "button_submit": button_submit, "error_password": error_password}
            return render(request, "password_recovery/redirect_p.html", context=data)

        else:
            messages.error(request, "Вы ввели неверный код/пароль!")
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "button_submit": button_submit, "error_password": error_password}
            return render(request, "password_recovery/password_recovery_sending.html", context=data)


def main(request):
    user_email = request.session.get("user_email")
    user = Users.objects.filter(email=user_email).first()
    user_id = user.id if user else None
    data = {"user_email": user_email, "user_id": user_id}
    return render(request, "main/main.html", context=data)


def main_sending(request):
    user_email = request.session.get("user_email")
    user = Users.objects.filter(email=user_email).first()
    user_id = user.id if user else None

    table = request.POST["table"]
    action = request.POST["action"]

    if action == "show_all":
        model = apps.get_model("django_app", table)
        fields = model._meta.get_fields()
        field_name_raw = [field.name for field in fields]
        if table == "Subjects":
            field_name_t = field_name_raw[3:]
            field_name = field_name_t
        elif table == "Listeners":
            field_name_t = field_name_raw[5:]
            field_name = field_name_t
        else:
            field_name = field_name_raw
        table_data = [(str(data_t)).split() for data_t in model.objects.all()]
        data = {"user_email": user_email, "user_id": user_id, "field_data": field_name, "table_data": table_data}
        return render(request, "main/main.html", context=data)

    elif action == "add_data":
        if table == "Subjects":
            fields = ["<h4>Название предмета</h4><input name='name_subject'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Teachers":
            fields = ["<h4>Фамилия преподавателя</h4><input name='surname_teacher'>",
                      "<h4>Имя преподавателя</h4><input name='name_teacher'>",
                      "<h4>Отчество преподавателя</h4><input name='patronymic_teacher'>",
                      "<h4>ID предмета</h4><input name='subject_id' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Listeners":
            fields = ["<h4>Фамилия студента</h4><input name='surname_listener'>",
                      "<h4>Имя студента</h4><input name='name_listener'>",
                      "<h4>Отчество студента</h4><input name='patronymic_listener'>",
                      "<h4>ID предмета</h4><input name='subject_id' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "AcademicRecords":
            fields = ["<h4>ID студента</h4><input name='listener_id' type='number'>",
                      "<h4>Оценка</h4><input name='mark' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            messages.warning(request, "В не обладаете правами доступа к данной таблице!")
            fields = ["<h4>Эта таблица и действия с ней доступны только админестраторам! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

        else:
            fields = ["<h4>ID студента</h4><input name='listener_id' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

    elif action == "change":
        if table == "Subjects":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>",
                      "<h4>Название предмета</h4><input name='name_subject'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Teachers":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>",
                      "<h4>Фамилия преподавателя</h4><input name='surname_teacher'>",
                      "<h4>Имя преподавателя</h4><input name='name_teacher'>",
                      "<h4>Отчество преподавателя</h4><input name='patronymic_teacher'>",
                      "<h4>ID предмета</h4><input name='subject_id' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Listeners":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>",
                      "<h4>Фамилия студента</h4><input name='surname_listener'>",
                      "<h4>Имя студента</h4><input name='name_listener'>",
                      "<h4>Отчество студента</h4><input name='patronymic_listener'>",
                      "<h4>ID предмета</h4><input name='subject_id' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "AcademicRecords":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>",
                      "<h4>Оценка</h4><input name='mark' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            messages.warning(request, "В не обладаете правами доступа к данной таблице!")
            fields = ["<h4>Эта таблица и действия с ней доступны только админестраторам! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

        else:
            messages.warning(request, "Тут нечего делать!")
            fields = ["<h4>Тут вам делать нечего! Все поля подтягиваются автоматически из БД!</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

    else:
        if table != "Users":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Удалить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Удалить</button>"}
            return render(request, "main/main_aud.html", context=data)
        else:
            messages.warning(request, "В не обладаете правами доступа к данной таблице!")
            fields = ["<h4>Эта таблица и действия с ней доступны только админестраторам! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)


def main_root(request):
    fields = ["<h4>ID пользователя</h4><input name='id_user' type='number'>",
              "<h4>Тип пользователя</h4><input name='type_user'>"]
    data = {"table_name": "Users", "fields": fields,
            "button": "<button name='button' type='submit' value='Выдать'>Выдать</button>"}
    return render(request, "main/main_aud.html", context=data)


def main_aud(request):
    user_email = request.session.get("user_email")
    user = Users.objects.filter(email=user_email).first()
    user_id = user.id if user else None

    table = request.POST.get("table_name", "-undefined-")
    button = request.POST.get("button", "-undefined-")

    if button == "Добавить":
        if table == "Subjects":
            name_subject = request.POST.get("name_subject", "-undefined-")
            fields = [f"<h4>Название предмета</h4><input name='name_subject' value='{name_subject}'>"]
            if name_subject != "":
                subject = Subjects(
                    name_subject=name_subject,
                    id_creator=user_id
                )
                subject.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Teachers":
            surname_teacher = request.POST.get("surname_teacher", "-undefined-")
            name_teacher = request.POST.get("name_teacher", "-undefined-")
            patronymic_teacher = request.POST.get("patronymic_teacher", "-undefined-")
            subject_id_raw = request.POST.get("subject_id", "-undefined-")
            try:
                subject_id = int(subject_id_raw)
            except (ValueError, TypeError):
                subject_id = None
            subject_id_key = Subjects.objects.filter(id=subject_id)
            fields = [f"<h4>Фамилия преподавателя</h4><input name='surname_teacher' value='{surname_teacher}'>",
                      f"<h4>Имя преподавателя</h4><input name='name_teacher' value='{name_teacher}'>",
                      f"<h4>Отчество преподавателя</h4><input name='patronymic_teacher' value='{patronymic_teacher}'>",
                      f"<h4>ID предмета</h4><input name='subject_id' type='number' value='{subject_id}'>"]
            if surname_teacher != "" and name_teacher != "" and patronymic_teacher != "" and subject_id != "" and subject_id_key:
                teacher = Teachers(
                    surname_teacher=surname_teacher,
                    name_teacher=name_teacher,
                    patronymic_teacher=patronymic_teacher,
                    subject_id=subject_id,
                    id_creator=user_id
                )
                teacher.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Listeners":
            surname_listener = request.POST.get("surname_listener", "-undefined-")
            name_listener = request.POST.get("name_listener", "-undefined-")
            patronymic_listener = request.POST.get("patronymic_listener", "-undefined-")
            subject_id = request.POST.get("subject_id", "-undefined-")
            subject_id_key = Subjects.objects.filter(id=subject_id).exists()
            fields = [f"<h4>Фамилия студента</h4><input name='surname_listener' value='{surname_listener}'>",
                      f"<h4>Имя студента</h4><input name='name_listener' value='{name_listener}'>",
                      f"<h4>Отчество студента</h4><input name='patronymic_listener' value='{patronymic_listener}'>",
                      f"<h4>ID предмета</h4><input name='subject_id' type='number' value='{subject_id}'>"]
            if surname_listener != "" and name_listener != "" and patronymic_listener != "" and subject_id != "" and subject_id_key:
                listener = Listeners(
                    surname_listener=surname_listener,
                    name_listener=name_listener,
                    patronymic_listener=patronymic_listener,
                    subject_id=subject_id,
                    id_creator=user_id
                )
                listener.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "AcademicRecords":
            listener_id = request.POST.get("listener_id", "-undefined-")
            mark = request.POST.get("mark", "-undefined-")
            id_listener = Listeners.objects.filter(id=listener_id)
            fields = [f"<h4>ID студента</h4><input name='listener_id' type='number' value='{listener_id}'>",
                      f"<h4>Оценка</h4><input name='mark' type='number' value='{mark}'>"]
            if listener_id != "" and mark != "" and id_listener:
                listener = Listeners.objects.get(id=listener_id)
                academ = AcademicRecords(
                    surname_listener=listener.surname_listener,
                    name_listener=listener.name_listener,
                    patronymic_listener=listener.patronymic_listener,
                    subject_id=listener.subject_id,
                    listener_id=listener_id,
                    mark=mark,
                    id_creator=user_id
                )
                academ.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            pass

        else:
            listener_id = request.POST.get("listener_id", "-undefined-")
            model = apps.get_model("django_app", table)
            id_listener = Listeners.objects.filter(id=listener_id)
            fields = [f"<h4>ID студента</h4><input name='listener_id' type='number' value='{listener_id}'>"]
            if listener_id != "" and id_listener:
                listener = Listeners.objects.get(id=listener_id)
                stud = model(
                    surname_listener=listener.surname_listener,
                    name_listener=listener.name_listener,
                    patronymic_listener=listener.patronymic_listener,
                    listener_id=listener_id,
                    id_creator=user_id
                )
                stud.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

    elif button == "Изменить":
        if table == "Subjects":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            name_subject = request.POST.get("name_subject", "-undefined-")
            data_id = Subjects.objects.filter(id=id_data).exists()
            fields = [f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                      f"<h4>Название предмета</h4><input name='name_subject' value='{name_subject}'>"]
            if id_data is not None and name_subject != "" and data_id:
                data_list = Subjects.objects.get(id=id_data)
                if user_type == "Super_Admin" or user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.name_subject = name_subject
                    data_list.save()
                    messages.success(request, "Запись успешно обновлена!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/redirect_m.html", context=data)
                else:
                    messages.error(request, "Вы не можете изменять чужие данные!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/main_aud.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Teachers":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            surname_teacher = request.POST.get("surname_teacher", "-undefined-")
            name_teacher = request.POST.get("name_teacher", "-undefined-")
            patronymic_teacher = request.POST.get("patronymic_teacher", "-undefined-")
            subject_id_raw = request.POST.get("subject_id", "-undefined-")
            try:
                subject_id = int(subject_id_raw)
            except (ValueError, TypeError):
                subject_id = None
            subject_id_key_raw = Subjects.objects.filter(id=subject_id).exists()
            try:
                subject_id_key = int(subject_id_key_raw)
            except (ValueError, TypeError):
                subject_id_key = None
            data_id = Teachers.objects.filter(id=id_data).exists()
            fields = [f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                      f"<h4>Фамилия преподавателя</h4><input name='surname_teacher' value='{surname_teacher}'>",
                      f"<h4>Имя преподавателя</h4><input name='name_teacher' value='{name_teacher}'>",
                      f"<h4>Отчество преподавателя</h4><input name='patronymic_teacher' value='{patronymic_teacher}'>",
                      f"<h4>ID предмета</h4><input name='subject_id' type='number' value='{subject_id}'>"]
            if id_data is not None and surname_teacher != "" and name_teacher != "" and patronymic_teacher != "" and subject_id is not None and subject_id_key and data_id:
                data_list = Teachers.objects.get(id=id_data)
                if user_type == "Super_Admin" or user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.surname_teacher = surname_teacher
                    data_list.name_teacher = name_teacher
                    data_list.patronymic_teacher = patronymic_teacher
                    data_list.save()
                    messages.success(request, "Запись успешно обновлена!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/redirect_m.html", context=data)
                else:
                    messages.error(request, "Вы не можете изменять чужие данные!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/main_aud.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Listeners":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            surname_listener = request.POST.get("surname_listener", "-undefined-")
            name_listener = request.POST.get("name_listener", "-undefined-")
            patronymic_listener = request.POST.get("patronymic_listener", "-undefined-")
            subject_id_raw = request.POST.get("subject_id", "-undefined-")
            try:
                subject_id = int(subject_id_raw)
            except (ValueError, TypeError):
                subject_id = None
            subject_id_key_raw = Subjects.objects.filter(id=subject_id).exists()
            try:
                subject_id_key = int(subject_id_key_raw)
            except (ValueError, TypeError):
                subject_id_key = None
            data_id = Listeners.objects.filter(id=id_data)
            fields = [f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                      f"<h4>Фамилия студента</h4><input name='surname_listener' value='{surname_listener}'>",
                      f"<h4>Имя студента</h4><input name='name_listener' value='{name_listener}'>",
                      f"<h4>Отчество студента</h4><input name='patronymic_listener' value='{patronymic_listener}'>",
                      f"<h4>ID предмета</h4><input name='subject_id' type='number' value='{subject_id}'>"]
            if id_data is not None and surname_listener != "" and name_listener != "" and patronymic_listener != "" and subject_id is not None and subject_id_key and data_id:
                data_list = Listeners.objects.get(id=id_data)
                if user_type == "Super_Admin" or user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.surname_listener = surname_listener
                    data_list.name_listener = name_listener
                    data_list.patronymic_listener = patronymic_listener
                    data_list.subject_id = subject_id
                    data_list.save()
                    messages.success(request, "Запись успешно обновлена!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/redirect_m.html", context=data)
                else:
                    messages.error(request, "Вы не можете изменять чужие данные!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/main_aud.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "AcademicRecords":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            mark = request.POST.get("mark", "-undefined-")
            data_id = AcademicRecords.objects.filter(id=id_data)
            fields = [f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                      f"<h4>Оценка</h4><input name='mark' type='number' value='{mark}'>"]
            if id_data is not None and mark != "" and data_id:
                data_list = AcademicRecords.objects.get(id=id_data)
                if user_type == "Super_Admin" or user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.mark = mark
                    data_list.save()
                    messages.success(request, "Запись успешно обновлена!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/redirect_m.html", context=data)
                else:
                    messages.error(request, "Вы не можете изменять чужие данные!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                    return render(request, "main/main_aud.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            pass

        else:
            pass

    elif button == "Удалить":
        if table != "Users":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            model = apps.get_model("django_app", table)
            data_id = model.objects.filter(id=id_data)
            fields = [f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>"]
            if id_data != "" and data_id:
                data_list = model.objects.get(id=id_data)
                if user_type == "Super_Admin" or user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.delete()
                    messages.success(request, "Запись успешно удалена!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Удалить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Удалить</button>"}
                    return render(request, "main/redirect_m.html", context=data)
                else:
                    messages.error(request, "Вы не можете удалять чужие данные!")
                    data = {"table_name": table, "fields": fields,
                            "button": "<button name='button' type='submit' value='Удалить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Удалить</button>"}
                    return render(request, "main/main_aud.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Удалить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Удалить</button>"}
                return render(request, "main/main_aud.html", context=data)
        else:
            pass
