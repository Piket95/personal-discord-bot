FROM python:3.14.0rc1-alpine
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "-u", "main.py"]