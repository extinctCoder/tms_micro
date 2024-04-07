FROM python:3.11

WORKDIR /src
RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY ./Pipfile .
RUN pipenv lock && pipenv install --system --deploy

COPY ./src .

EXPOSE 8000
RUN python3 auth_service/main.py