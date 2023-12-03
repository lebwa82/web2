# установка базового образа (host OS)
FROM python:3.11

# установка рабочей директории в контейнере
WORKDIR /hw10/subscriber

# копирование содержимого локальной директории src в рабочую директорию
COPY . /hw10/subscriber

# установка зависимостей
RUN pip install -r /hw10/subscriber/requirements.txt
RUN chmod +x wait-for-it.sh

# команда, выполняемая при запуске контейнера
# CMD ["python", "subscriber.py" ]