up:
	docker-compose up -d --build
down:
	docker-compose down -v

logs:
	docker-compose logs -f

docker-build:
	docker build -t rozarioagro/praktikum-api-yambd:v1 .

docker-push:
	docker push rozarioagro/praktikum-api-yambd:v1


init-fake-data: flush-db add-super seed_fake_users seed_fake_genres	seed_fake_categories seed_fake_titles seed_fake_reviews_comments
init-file-data: flush-db add-super seed_file_users seed_file_genres seed_file_categories seed_file_titles seed_file_reviews_comments

make-translations:
	django-admin makemessages -l ru -e py -i venv
compile-translations:
	django-admin compilemessages --exclude venv

flush-db:
	./manage.py flush --no-input

add-super:
	./manage.py createsuperuser

seed_fake_users:
	./manage.py seed_fake_users
seed_fake_genres:
	./manage.py seed_fake_genres
seed_fake_categories:
	./manage.py seed_fake_categories
seed_fake_titles:
	./manage.py seed_fake_titles

seed_fake_reviews_comments:
	./manage.py seed_fake_reviews_comments


seed_file_users:
	./manage.py seed_users_from_file
seed_file_genres:
	./manage.py seed_genres_from_file
seed_file_categories:
	./manage.py seed_categories_from_file
seed_file_titles:
	./manage.py seed_titles_from_file

seed_file_reviews_comments:
	./manage.py seed_reviews_and_comments_from_file