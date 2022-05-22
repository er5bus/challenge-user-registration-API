# temp stage
FROM python:3.9-buster as compile-image

WORKDIR /app

RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./src/setup.py .

COPY ./src /app/src

RUN pip install .

# final stage
FROM er5bus/python-usd:python3.9-slim

RUN addgroup --system fastapi \
  && adduser --system --ingroup fastapi fastapi

COPY --from=compile-image --chown=fastapi:fastapi /opt/venv /opt/venv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

USER fastapi

CMD gunicorn src.main:app -w 2 -k uvicorn.workers.UvicornWorker -b "0.0.0.0:8080"
