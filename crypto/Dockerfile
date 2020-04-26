FROM ivonet/crypto-base:latest

COPY app /opt/app
COPY ivonet /usr/local/lib/python3.8/site-packages/ivonet

WORKDIR /opt/app

CMD ["python3", "app.py", "--host", "0.0.0.0"]
