
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
                <p style="font-size: 9px;">Почта должна быть в виде pochta@email.ru</p>'''
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
                type="Admin",
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
        if table == "User":
            field_name_t = field_name_raw[1:]
            field_name = field_name_t
        elif table == "Community":
            field_name_t = field_name_raw[1:]
            field_name = field_name_t
        elif table == "Subscribers_subscriptions":
            field_name_t = field_name_raw
            field_name = field_name_t
        else:
            field_name_t = field_name_raw
            field_name = field_name_t
        table_data = [(str(data_t)).split() for data_t in model.objects.all()]
        data = {"user_email": user_email, "user_id": user_id, "field_data": field_name, "table_data": table_data}
        return render(request, "main/main.html", context=data)

    elif action == "add_data":
        if table == "User":
            fields = [
                f"<h4>Имя</h4><input name='first_name'>"
                f"<h4>Фамилия</h4><input name='last_name'>",
                f"<h4>Дата рождения</h4><input name='birthday'>",
                f"<h4>Возраст</h4><input name='user_age'type='number'>",
                f"<h4>Дата регестрации</h4><input name='registration_date'>"
                f"<h4>Страна</h4><input name='country'>",
                f"<h4>Город</h4><input name='city'>",
                f"<h4>Район</h4><input name='district'>"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Community":
            fields = [
                f"<h4>Название сообщества</h4><input name='community_name'>",
                f"<h4>Описание сообщества</h4><input name='community_description'>",
                f"<h4>Страна</h4><input name='country'>",
                f"<h4>Город</h4><input name='city'>",
                f"<h4>Район</h4><input name='district'>"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Subscribers_subscriptions":
            fields = [
                f"<h4>ID пользователя</h4><input name='surname_listener' >",
                f"<h4>ID сообщества</h4><input name='name_listener' >"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            messages.warning(request, "Нет прав доступа!")
            fields = ["<h4>Эта таблица не может быть изменена из интерфейса! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

    elif action == "change":
        if table == "User":
            fields = [
                f"<h4>ID записи</h4><input name='first_name' type='number'>"
                f"<h4>Имя</h4><input name='first_name'>"
                f"<h4>Фамилия</h4><input name='last_name'>",
                f"<h4>Дата рождения</h4><input name='birthday'>",
                f"<h4>Возраст</h4><input name='user_age'type='number'>",
                f"<h4>Дата регестрации</h4><input name='registration_date'>"
                f"<h4>Страна</h4><input name='country'>",
                f"<h4>Город</h4><input name='city'>",
                f"<h4>Район</h4><input name='district'>"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Community":
            fields = [
                f"<h4>ID записи</h4><input name='first_name' type='number'>"
                f"<h4>Название сообщества</h4><input name='community_name'>",
                f"<h4>Описание сообщества</h4><input name='community_description'>",
                f"<h4>Страна</h4><input name='country'>",
                f"<h4>Город</h4><input name='city'>",
                f"<h4>Район</h4><input name='district'>"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Subscribers_subscriptions":
            fields = [
                f"<h4>ID записи</h4><input name='first_name' type='number'>"
                f"<h4>ID пользователя</h4><input name='surname_listener' >",
                f"<h4>ID сообщества</h4><input name='name_listener' >"
            ]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Изменить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Изменить</button>"}
            return render(request, "main/main_aud.html", context=data)

        elif table == "Users":
            messages.warning(request, "Нет прав доступа!")
            fields = ["<h4>Эта таблица и действия с ней доступны только админестраторам! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

        else:
            messages.warning(request, "Нет прав доступа!")
            fields = ["<h4>Эта таблица не может быть изменена из интерфейса! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
            data = {"table_name": table, "fields": fields}
            return render(request, "main/main_aud.html", context=data)

    else:
        if table != "Users":
            fields = ["<h4>ID записи</h4><input name='id_data' type='number'>"]
            data = {"table_name": table, "fields": fields,
                    "button": "<button name='button' type='submit' value='Удалить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Удалить</button>"}
            return render(request, "main/main_aud.html", context=data)
        else:
            messages.warning(request, "Нет прав доступа!")
            fields = ["<h4>Эта таблица не может быть изменена из интерфейса! Для возврата к таблицам нажмите кнопку 'Назад'</h4>"]
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
        if table == "User":
            first_name = request.POST.get("first_name", "-undefined-")
            last_name = request.POST.get("last_name", "-undefined-")
            birthday = request.POST.get("birthday", "-undefined-")
            user_age = request.POST.get("user_age", "-undefined-")
            registration_date = request.POST.get("registration_date", "-undefined-")
            country = request.POST.get("country", "-undefined-")
            city = request.POST.get("city", "-undefined-")
            district = request.POST.get("district", "-undefined-")
            fields = [
                f"<h4>Имя</h4><input name='first_name' value='{first_name}'>"
                f"<h4>Фамилия</h4><input name='last_name' value='{last_name}'>",
                f"<h4>Дата рождения</h4><input name='birthday' value='{birthday}'>",
                f"<h4>Возраст</h4><input name='user_age'type='number' value='{user_age}'>",
                f"<h4>Дата регестрации</h4><input name='registration_date' value='{registration_date}'>"
                f"<h4>Страна</h4><input name='country' value='{country}'>",
                f"<h4>Город</h4><input name='city' value='{city}'>",
                f"<h4>Район</h4><input name='district'  value='{district}'>"
            ]
            if first_name != "" and last_name != "" and birthday != "" and user_age != "" and registration_date != "" and country != "" and city != "" and district != "":
                user_tabel = User(
                    first_name=first_name,
                    last_name=last_name,
                    birthday=birthday,
                    user_age=user_age,
                    registration_date=registration_date,
                    country=country,
                    city=city,
                    district=district,
                    id_creator=user_id
                )
                user_tabel.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Community":
            community_name = request.POST.get("community_name", "-undefined-")
            community_description = request.POST.get("community_description", "-undefined-")
            country = request.POST.get("country", "-undefined-")
            city = request.POST.get("city", "-undefined-")
            district = request.POST.get("district", "-undefined-")
            fields = [
                      f"<h4>Название сообщества</h4><input name='community_name' value='{community_name}'>",
                      f"<h4>Описание сообщества</h4><input name='community_description' value='{community_description}'>",
                      f"<h4>Страна</h4><input name='country' value='{country}'>",
                      f"<h4>Город</h4><input name='city' value='{city}'>"
                      f"<h4>Район</h4><input name='district' value='{district}'>"
                      ]
            if community_name != "" and community_description != "" and country != "" and city != "" and district != "":
                community = Community(
                    community_name=community_name,
                    community_description=community_description,
                    country=country,
                    city=city,
                    district=district,
                    id_creator=user_id
                )
                community.save()
                messages.success(request, "Запись успешно добавлена!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/redirect_m.html", context=data)
            else:
                messages.error(request, "Введите корректные данные!")
                data = {"table_name": table, "fields": fields,
                        "button": "<button name='button' type='submit' value='Добавить' class='btn btn-primary' style='color: #D2D2D2; background-color: #FF4C2B; border-color: #FF4C2B;'>Добавить</button>"}
                return render(request, "main/main_aud.html", context=data)

        elif table == "Subscribers_subscriptions":
            user_tabel_id = request.POST.get("user_tabel_id", "-undefined-")
            community_id = request.POST.get("community_id", "-undefined-")
            try:
                user_tabel_id = int(user_tabel_id)
            except (ValueError, TypeError):
                user_tabel_id = None
            try:
                community_id = int(community_id)
            except (ValueError, TypeError):
                community_id = None
            user_id_key = User.objects.filter(id=user_tabel_id).exists()
            community_id_key = Community.objects.filter(id=community_id).exists()
            fields = [
                      f"<h4>ID пользователя</h4><input name='surname_listener' type='number' value='{user_tabel_id}'>",
                      f"<h4>ID сообщества</h4><input name='name_listener' type='number' value='{community_id}'>"
                      ]
            if user_id_key and community_id_key:
                subscribers_subscriptions = Subscribers_subscriptions(
                    user_id=user_tabel_id,
                    community_id=community_id,
                    id_creator=user_id
                )
                subscribers_subscriptions.save()
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

    elif button == "Изменить":
        if table == "User":
            user_type = user.type
            id_data_raw = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data_raw)
            except (ValueError, TypeError):
                id_data = None
            first_name = request.POST.get("first_name", "-undefined-")
            last_name = request.POST.get("last_name", "-undefined-")
            birthday = request.POST.get("birthday", "-undefined-")
            user_age = request.POST.get("user_age", "-undefined-")
            registration_date = request.POST.get("registration_date", "-undefined-")
            country = request.POST.get("country", "-undefined-")
            city = request.POST.get("city", "-undefined-")
            district = request.POST.get("district", "-undefined-")
            data_id = User.objects.filter(id=id_data).exists()
            fields = [
                f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                f"<h4>Имя</h4><input name='first_name' value='{first_name}'>"
                f"<h4>Фамилия</h4><input name='last_name' value='{last_name}'>",
                f"<h4>Дата рождения</h4><input name='birthday' value='{birthday}'>",
                f"<h4>Возраст</h4><input name='user_age'type='number' value='{user_age}'>",
                f"<h4>Дата регестрации</h4><input name='registration_date' value='{registration_date}'>"
                f"<h4>Страна</h4><input name='country' value='{country}'>",
                f"<h4>Город</h4><input name='city' value='{city}'>",
                f"<h4>Район</h4><input name='district'  value='{district}'>"
            ]
            if id_data is not None and first_name != "" and last_name != "" and birthday != "" and user_age != "" and registration_date != "" and country != "" and city != "" and district != ""  and data_id:
                data_list = User.objects.get(id=id_data)
                if user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.first_name = first_name
                    data_list.last_name = last_name
                    data_list.birthday = birthday
                    data_list.user_age = user_age
                    data_list.country = country
                    data_list.city = city
                    data_list.district = district
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

        elif table == "Community":
            user_type = user.type
            id_data = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data)
            except (ValueError, TypeError):
                id_data = None
            community_name = request.POST.get("community_name", "-undefined-")
            community_description = request.POST.get("community_description", "-undefined-")
            country = request.POST.get("country", "-undefined-")
            city = request.POST.get("city", "-undefined-")
            district = request.POST.get("district", "-undefined-")
            data_id = Community.objects.filter(id=id_data).exists()
            fields = [
                f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                f"<h4>Название сообщества</h4><input name='community_name' value='{community_name}'>",
                      f"<h4>Описание сообщества</h4><input name='community_description' value='{community_description}'>",
                      f"<h4>Страна</h4><input name='country' value='{country}'>",
                      f"<h4>Город</h4><input name='city' value='{city}'>"
                      f"<h4>Район</h4><input name='district' value='{district}'>"
            ]
            if id_data is not None and community_name != "" and community_description != "" and country != "" and city != "" and district != "" and data_id:
                data_list = Community.objects.get(id=id_data)
                if user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.community_name = community_name
                    data_list.community_description = community_description
                    data_list.country = country
                    data_list.city = city
                    data_list.district = district
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

        elif table == "Subscribers_subscriptions":
            user_type = user.type
            id_data = request.POST.get("id_data", "-undefined-")
            try:
                id_data = int(id_data)
            except (ValueError, TypeError):
                id_data = None
            user_tabel_id = request.POST.get("user_id", "-undefined-")
            community_id = request.POST.get("community_id", "-undefined-")
            try:
                user_tabel_id = int(user_tabel_id)
            except (ValueError, TypeError):
                user_tabel_id = None
            user_id_key_raw = User.objects.filter(id=user_tabel_id).exists()
            try:
                community_id = int(community_id)
            except (ValueError, TypeError):
                community_id = None
            community_id_key_raw = Community.objects.filter(id=community_id).exists()
            data_id = Subscribers_subscriptions.objects.filter(id=id_data)
            fields = [
                        f"<h4>ID записи</h4><input name='id_data' type='number' value='{id_data}'>",
                        f"<h4>ID пользователя</h4><input name='surname_listener' type='number' value='{user_tabel_id}'>",
                        f"<h4>ID сообщества</h4><input name='name_listener' type='number' value='{community_id}'>"
                    ]
            if id_data is not None and user_id_key_raw and community_id_key_raw and data_id:
                data_list = Subscribers_subscriptions.objects.get(id=id_data)
                if user_type == "Admin" or data_list.id_creator == user_id:
                    data_list.user = user_tabel_id
                    data_list.community = community_id
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
                if user_type == "Admin" or data_list.id_creator == user_id:
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
