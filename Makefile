make-translations:
	django-admin makemessages -l ru -e py -i venv
compile-translations:
	django-admin compilemessages --exclude venv

up:
	docker-compose up -d --build
down:
	docker-compose down -v

logs:
	docker-compose logs -f

docker-build:
	docker build -t rozarioagro/avipy-gateway:v1 .

docker-push:
	docker push rozarioagro/avipy-gateway:v1