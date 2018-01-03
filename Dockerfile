FROM python:2.7.14-alpine3.6

COPY entrypoint.sh .
RUN chmod +x /entrypoint.sh

COPY listener.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
