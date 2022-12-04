FROM python:3.9

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver"]
EXPOSE 8000