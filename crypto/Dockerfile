FROM ivonet/crypto-base:latest

ENV DEBUG=0

COPY app /opt/app
COPY ivonet /usr/local/lib/python3.9/site-packages/ivonet

WORKDIR /opt/app

EXPOSE 5000
CMD ["python3", "app.py", "--bind", "0.0.0.0", "--port", "5000"]
