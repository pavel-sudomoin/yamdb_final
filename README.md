# api_yamdb
api_yamdb

Тут добавлены 3 приложения:

     artworks - для произведений, жанров и категорий
     reviews - для отзывов и комментов к ним
     users - для пользователей 

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
-------------------------------------------

###User
Внести пользователей в БД из предложенного файла
- python manage.py seed_users_from_file

либо более суровый вариант используя Faker
- python manage.py seed_fake_users

-------------------------------------------