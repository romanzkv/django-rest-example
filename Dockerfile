# Use the Debian buster image as the base
FROM python:3.12.0a4-bullseye

EXPOSE 8000
# Set the working directory to the app directory
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt 

# Run the main Python file
CMD [ "./run-server.sh" ]
