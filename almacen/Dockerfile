# We Use an official Python runtime as a parent image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /almacen_service

# Set the working directory to /almacen_service
WORKDIR /almacen_service

# Copy the current directory contents into the container at /almacen_service
ADD . /almacen_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD gunicorn -b :8000 django.wsgi
