FROM python:3.9-alpine3.13
LABEL maintainer="{{ cookiecutter.email }}"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

# Separate python dependency from docker image
# Add app user
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

# Add python package in virturalenv to path
ENV PATH="/py/bin:$PATH"

USER app