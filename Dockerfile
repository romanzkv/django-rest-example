# Use the Debian buster image as the base
FROM python:3.12.0a4-bullseye

# Set the working directory to the app directory
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt 

# Run the main Python file
CMD [ "sleep", "100000" ]
