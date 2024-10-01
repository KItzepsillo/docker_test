FROM python:3.11-slim-buster

# Install python package
COPY ./docker/mlflow/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
