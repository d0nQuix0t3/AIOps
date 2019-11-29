FROM python:3.7
ADD ./apps/apm-flask /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py