make-translations:
	django-admin makemessages -l ru -e py -i venv
compile-translations:
	django-admin compilemessages --exclude venv