# Use the Debian buster image as the base
FROM python:3.12.0a4-bullseye

RUN pip install -r requirements.txt 

# Set the working directory to the app directory
WORKDIR /app

# Run the main Python file
CMD [ "sleep", "100000" ]
