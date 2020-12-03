# Спринт 18 для Yandex.Praktikum - запуск docker-контейнеров с проектом YaMDb

## Описание проекта

Проект представляет собой REST API для сервиса YaMDb - базы отзывов о фильмах, книгах и музыке

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Читатели могут оставлять к произведениям текстовые отзывы (Review) и выставлять произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.

Проект разработан в учебных целях как спринт 18 для **Yandex.Praktikum**.

## Установка проекта

Клонируйте данный репозиторий на свой компьютер и перейдите в папку проекта.

После выполнения указанных ниже команд на вашем компьютере в двух docker-контейнерах будет развёрнут проект YaMDb. Будет поднят один docker-контейнер с web-приложением и один с базой данных.

### Установка docker и docker-compose

Для установки docker и docker-compose воспользуйтесь официальной [инструкцией](https://docs.docker.com/get-docker/).

### Структура файла *.env* с переменными окружения

Переменные окружения хранятся в файле *.env*. Вы можете изменять его и задавать собственные настройки и пароли.

По умолчанию файл имеет следующую структуру:

<pre><code>
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (рекомендуется установить свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
</code></pre>

### Сборка и запуск контейнеров

<pre><code>sudo docker-compose up</code></pre>

### Миграция базы данных

<pre><code>sudo docker-compose run web python manage.py migrate</code></pre>

### Остановка контейнеров

<pre><code>sudo docker-compose down</code></pre>

## Работа с проектом

### Создание суперпользователя

<pre><code>sudo docker-compose run web python manage.py createsuperuser</code></pre>

### Заполнение базы начальными данными

<pre><code>sudo docker-compose run web python manage.py loaddata fixtures.json</code></pre>

## Авторы

* [Yandex.Praktikum](https://praktikum.yandex.ru/)

* [Роман Володин](https://github.com/RomanAVolodin/) - обработка создания пользователей

* [Николай Тихонов](https://github.com/optcond/) - обработка отзывов и комментариев к ним

* [Судомоин Павел](https://github.com/pavel-sudomoin/) - обработка произведений, жанров и категорий
