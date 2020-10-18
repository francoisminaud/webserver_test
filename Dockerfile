FROM python:3.6

RUN apt-get update

COPY wiremind_webserver.py /root/wiremind_webserver.py
EXPOSE 8001

CMD ["python3","/root/wiremind_webserver.py"]
