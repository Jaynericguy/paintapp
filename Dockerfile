FROM python:3

#ENV POSTGRES_DB $POSTGRES_DB
#ENV POSTGRES_USER $POSTGRES_USER
#ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
#ENV POSTGRES_HOST $POSTGRES_HOST
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /django

WORKDIR /django

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
