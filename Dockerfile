


# pull the official base image
FROM python:3.9.6

# set work directory
RUN mkdir /game_service
WORKDIR /game_service
RUN echo "Shiv Shankar Keshari"
ADD . /game_service/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN pip install gunicorn




EXPOSE 8000
# CMD ["/usr/local/bin/gunicorn", "pyui.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
# CMD ["python", "manage.py", "migrate"]

RUN python manage.py migrate
CMD ["python manage.py migrate", "python manage.py runserver 0.0.0.0:8000"]

# # docker build --tag django_game_service_image .
# # docker run --name django_game_service_container -d -p 8000:8000 django_game_service_image
# # docker ps
# # docker kill id
# # docker rm id
# # docker rmi django_game_service_image
