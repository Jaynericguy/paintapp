FROM python:3.11-alpine

#ENV POSTGRES_DB $POSTGRES_DB
#ENV POSTGRES_USER $POSTGRES_USER
#ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
#ENV POSTGRES_HOST $POSTGRES_HOST
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django
RUN apk add python3-dev build-base linux-headers pcre-dev libffi-dev libpq-dev postgresql-client
RUN pip install uwsgi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir /var/run/app-uwsgi
RUN chown -R root:root /var/run/app-uwsgi
CMD ["sh", "-c", "python manage.py collectstatic --noinput && uwsgi --ini app.uwsgi.ini"]
EXPOSE 8000
