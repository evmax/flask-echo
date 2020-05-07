FROM python:alpine

WORKDIR /app
COPY ./docker/entrypoint /app
COPY ./requirements/* ./requirements/
RUN pip install -r requirements/prod.txt
COPY ./src /app
ENV APP__LOG_PATH=/var/log/

RUN ["chmod", "+x", "/app/entrypoint"]
EXPOSE 5000
ENTRYPOINT ["/app/entrypoint"]

