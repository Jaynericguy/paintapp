FROM python:3.9

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000