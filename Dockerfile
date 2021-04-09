FROM python:3.6

COPY ./src /usr/src
WORKDIR /usr/src
EXPOSE 8000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]