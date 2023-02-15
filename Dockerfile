FROM python:3.9

WORKDIR /ApiGrupo3

COPY ./requirements.txt /ApiGrupo3/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ApiGrupo3/requirements.txt

EXPOSE 80

COPY ./app /ApiGrupo3/app

CMD ["uvicorn", "app.api:api", "--host", "0.0.0.0", "--port", "80"]