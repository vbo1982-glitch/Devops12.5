FROM ubuntu:22.04

RUN apt-get update && apt-get install -y apache2

RUN echo "<h1>Hello from AWS ECR Task!</h1>" > /var/www/html/index.html

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]