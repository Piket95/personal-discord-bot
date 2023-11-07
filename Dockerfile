FROM python:3.13-rc-slim
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "-u", "main.py"]