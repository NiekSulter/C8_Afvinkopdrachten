FROM tiangolo/uwsgi-nginx-flask:latest
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt