FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput