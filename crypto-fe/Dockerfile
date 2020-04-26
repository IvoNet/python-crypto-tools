FROM node:12.16.2-buster as builder

COPY . /opt/crypto
WORKDIR /opt/crypto

RUN npm install \
 && npm run build

FROM nginx:1.17.0

COPY --from=builder /opt/crypto/dist/crypto-fe /usr/share/nginx/html

EXPOSE 80

