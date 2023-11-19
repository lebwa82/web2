# установка базового образа (host OS)
FROM python:3.11

# установка рабочей директории в контейнере
WORKDIR /hw10/producer

# копирование содержимого локальной директории src в рабочую директорию
COPY . /hw10/producer
COPY requirements.txt /hw10/producer/requirements.txt

# установка зависимостей
RUN pip install -r /hw10/producer/requirements.txt

# команда, выполняемая при запуске контейнера
CMD ["python", "producer.py"]