FROM python:3.9

COPY . .
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]
EXPOSE 80