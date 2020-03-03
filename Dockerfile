# Inherit from the Python Docker image
FROM python:3.7-slim

COPY . /email_processing/
WORKDIR /email_processing/

# Install python packages
RUN pip install azure.storage.blob
RUN pip install PyPDF2
RUN pip install pathlib

# Set "python" as the entry point
ENTRYPOINT ["python"]
# Set the command as the script name
CMD ["main.py"]