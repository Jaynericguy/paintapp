FROM python:3.9

#ENV POSTGRES_DB $POSTGRES_DB
#ENV POSTGRES_USER $POSTGRES_USER
#ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
#ENV POSTGRES_HOST $POSTGRES_HOST

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV POSTGRES_HOST=default.postgres
# https://stackoverflow.com/questions/34398632/docker-how-to-run-pip-requirements-txt-only-if-there-was-a-change
WORKDIR /app
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt --upgrade-strategy only-if-needed

COPY /app .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
