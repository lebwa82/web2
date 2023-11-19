# установка базового образа (host OS)
FROM python:3.11

# установка рабочей директории в контейнере
WORKDIR /hw10/subscriber

# копирование содержимого локальной директории src в рабочую директорию
COPY . /hw10/subscriber
COPY requirements.txt /hw10/subscriber/requirements.txt

# установка зависимостей
RUN pip install -r /hw10/subscriber/requirements.txt

# команда, выполняемая при запуске контейнера
CMD ["python", "subscriber.py" ]