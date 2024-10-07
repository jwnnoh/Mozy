#
FROM python:3.12

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir -r /code/requirements.txt && \
    pip install "fastapi[standard]"

#
COPY ./app /code/app

#
COPY ./.env /code/.env

#
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
