FROM python:3.6.5-slim-stretch

COPY /deploy/requirements.txt /deploy/requirements.txt
RUN pip install --no-cache-dir --disable-pip-version-check --requirement /deploy/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV WEB_CONCURRENCY=4
ENV PORT ${PORT:-80}
EXPOSE $PORT

RUN mkdir /app
WORKDIR /app

COPY "$PWD/fixtures" /app/fixtures
COPY "$PWD/docker-entrypoint.sh" /app/docker-entrypoint.sh
COPY "$PWD/joplin" /app/joplin

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "joplin.wsgi:application", "--pythonpath", "/app/joplin"]
