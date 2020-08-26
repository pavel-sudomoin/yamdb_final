# api_yamdb
Клонируйте себе репозиторий, затем в каталоге проекта создайте свою ветку и перейдите на нее

git checkout -b develop 

и можно приступать :)

Тут добавлены 3 приложения:

     artworks - для произведений, жанров и категорий
     reviews - для отзывов и комментов к ним
     users - для пользователей 

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser

В настройках приложения уже добавлены JWTAuthentication, DjangoFilterBackend и PageNumberPagination 

По умолчанию доступ только для авторизованных пользователей

В модуле users есть файлик rbac.py в нем полезные классы permission AnyoneCanSeeListAdminCanEdit - подойдет для artwork и AnyoneCanSeeAdminModerAuthorCanEdit - для review

-------------------------------------------

###User
Внести пользователей в БД из предложенного файла
- python manage.py seed_users_from_file

либо более суровый вариант используя Faker
- python manage.py seed_fake_users

-------------------------------------------