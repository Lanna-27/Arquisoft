FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:4000
CMD ["sh", "-c", "python manage.py makemigrations swarch2024i_ms && python manage.py migrate && python manage.py runserver $URL"]

#docker run -p 4000:4000 -e DB_HOST=host.docker.internal -e DB_PORT=3306 -e DB_USER=swarch2024i -e DB_PASSWORD=2023 -e DB_NAME=swarch2024i_db -e URL=0.0.0.0:4000 swarch2024i_ms 